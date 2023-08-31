
import datetime
import pandas as pd
from typing import List, Dict


def get_unique_dates_count(data: List[Dict]) -> int:
    """
    Calculate the number of unique dates.
    """
    unique_dates = set()
    for job in data:
        start_dt = get_valid_dt(job.get('start'))
        end_dt = get_valid_dt(job.get('end'))
        dt_range = pd.date_range(start_dt, end_dt)
        for dt in dt_range:
            if dt.day == 1:
                unique_dates.add(dt.strftime('%Y-%m-%d'))
    return len(list(unique_dates))


def get_valid_dt(dt: str) -> str:
    """
    Convert a date string in 'MM.YYYY' format to a valid date in 'YYYY-MM-DD' format.
    """
    year, month = dt.split(".")
    return datetime.date(int(month), int(year), 1).strftime('%Y-%m-%d')


def valid_year(year: str):
    if len(year) == 4:
        return year
    return "20" + year


def valid_month(month: str):
    if len(month) == 2:
        return month
    return "0" + year


if __name__ == "__main__":
    data = []
    job_count = int(input("Введите количество работ: "))
    for i in range(1, job_count+1):
        start_dt = input(f"{i} введите начальную дату (MM.YYYY): ")
        start_month, start_year = start_dt.split('.')
        valid_start_dt = valid_month(start_month) + "." + valid_year(start_year)
        end_dt = input(f"{i} введите конечную дату (MM.YYYY): ")
        end_month, end_year = end_dt.split('.')
        valid_end_dt = valid_month(end_month) + "." + valid_year(end_year)
        data.append({"name": f"{i} job", 'start': valid_start_dt, 'end': valid_end_dt})


    print("unique dates count: " + str(get_unique_dates_count(data)))
