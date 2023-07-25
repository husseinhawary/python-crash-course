import unittest
from city_functions import get_city_country


class CityCountryTestCase(unittest.TestCase):

    def test_city_country(self):
        city_country = get_city_country("cairo", "egypt")
        self.assertEqual(city_country, "Cairo, Egypt")


if __name__ == "__main__":
    unittest.main()
