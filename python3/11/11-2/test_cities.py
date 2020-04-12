import unittest
from city_functions import city_country
from city_functions import city_country_population

class CityCountryCase(unittest.TestCase):
    """测试city_functions.py"""

    def test_city_country(self):
        """测试Santiago, Chile这样的字符串"""
        result_str = city_country('santiago','chile')
        self.assertEqual(result_str,'Santiago, Chile')

    def test_city_country_population(self):
        """测试Santiago, Chile这样的字符串"""
        result_str = city_country_population('santiago','chile')
        self.assertEqual(result_str,'Santiago, Chile')

    def test_city_country_population1(self):
        """测试Santiago, Chile - population 500000这样的字符串"""
        result_str = city_country_population('santiago','chile','500000')
        self.assertEqual(result_str,'Santiago, Chile - Population 500000')

unittest.main()
