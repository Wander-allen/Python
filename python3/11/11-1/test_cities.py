import unittest
from city_functions import city_country

class CityCountryCase(unittest.TestCase):
    """测试city_functions.py"""

    def test_city_country(self):
        """测试Santiago, Chile这样的字符串"""
        result_str = city_country('santiago','chile')
        self.assertEqual(result_str,'Santiago, Chile')

unittest.main()
