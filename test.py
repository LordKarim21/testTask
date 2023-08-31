from main import get_unique_dates_count
import unittest


class TestGetExpertise(unittest.TestCase):
    def setUp(self) -> None:
        self.data = [
            {
                'name': '1 job',
                'start': '05.2012',
                'end': '08.2015',
            },
            {
                'name': '2 job',
                'start': '03.2015',
                'end': '05.2018',
            },
            {
                'name': '3 job',
                'start': '04.2016',
                'end': '01.2020',
            },
        ]

    def test_unique_dates_count(self):
        result = get_unique_dates_count(self.data)
        self.assertEqual(result, 93)


if __name__ == '__main__':
    unittest.main()
