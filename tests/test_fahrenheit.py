import os
import sys
import unittest

module_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(module_dir, '../'))

from conversions import convertFahrenheitToCelsius, convertFahrenheitToKelvin

class TestFahrenheit(unittest.TestCase):
    """Fahrenheit Conversion Tests"""

    def test_fahrenheit_to_kelvin_with_300_should_be_422_039(self):
        self.assertEqual(convertFahrenheitToKelvin(300), 422.039)

    def test_fahrenheit_to_kelvin_with_5_should_be_258_15(self):
        self.assertEqual(convertFahrenheitToKelvin(5), 258.15) 

    def test_fahrenheit_to_kelvin_with_422(self):
        self.assertEqual(convertFahrenheitToKelvin(422), 489.817) 

    def test_fahrenheit_to_kelvin_with_0(self):
        self.assertEqual(convertFahrenheitToKelvin(0), 255.372) 

    def test_fahrenheit_to_kelvin_with_8(self):
        self.assertEqual(convertFahrenheitToKelvin(8), 259.817)