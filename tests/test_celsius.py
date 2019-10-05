import os
import sys
import unittest

module_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(module_dir, '../'))

from conversions import convertCelsiusToFahrenheit, convertCelsiustoKelvin

class TestCelsius(unittest.TestCase):
    """Test Conversion tests"""
    def test_celsius_to_kelvin_with_300_should_be_573_15(self):
        self.assertEqual(convertCelsiustoKelvin(300.00), 573.15)
        
    def test_celsius_to_kelvin_with_5_should_be_278_15(self):
        self.assertEqual(convertCelsiustoKelvin(5.0), 278.15)

    def test_celsius_to_kelvin_with_10_should_be_283_15(self):
        self.assertEqual(convertCelsiustoKelvin(10.0), 283.15)

    def test_celsius_to_kelvin_with_1030_should_be_1303_15(self):
        self.assertEqual(convertCelsiustoKelvin(1030.0), 1303.15)
    
    def test_celsius_to_kelvin_with_35_should_be_308_15(self):
        self.assertEqual(convertCelsiustoKelvin(35.0), 308.15)

    def test_celsius_to_fahrenheit_with_5_should_be_41(self):
        self.assertEqual(convertCelsiusToFahrenheit(5.0), 41)
    
    def test_celsius_to_fahrenheit_with_300_should_be_572(self):
        self.assertEqual(convertCelsiusToFahrenheit(300.0), 572)

    def test_celsius_to_fahrenheit_with_22_6_should_be_72_68(self):
        self.assertEqual(convertCelsiusToFahrenheit(22.6), 72.68)

    def test_celsius_to_fahrenheit_with_88_should_be_191_3(self):
        self.assertEqual(convertCelsiusToFahrenheit(88.5), 191.3)

    def test_celsius_to_fahrenheit_with_192_should_be_377_6(self):
        self.assertEqual(convertCelsiusToFahrenheit(192.0), 377.6)  