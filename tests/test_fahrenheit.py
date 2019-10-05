import os
import sys
import unittest

module_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(module_dir, '../'))

from conversions import convertFahrenheitToCelsius, convertFahrenheitToKelvin

class TestFahrenheit(unittest.TestCase):
    """Fahrenheit Conversion Tests"""

    def test_fahrenheit_to_kelvin_with_300_should_be_422_039(self):
        self.assertEqual(convertFahrenheitToKelvin(300.0), 422.039)

    def test_fahrenheit_to_kelvin_with_5_should_be_258_15(self):
        self.assertEqual(convertFahrenheitToKelvin(5.0), 258.15) 

    def test_fahrenheit_to_kelvin_with_422_should_be_489_817(self):
        self.assertEqual(convertFahrenheitToKelvin(422.0), 489.817) 

    def test_fahrenheit_to_kelvin_with_0_should_be_255_372(self):
        self.assertEqual(convertFahrenheitToKelvin(0.0), 255.372) 

    def test_fahrenheit_to_kelvin_with_8_should_be_259_817(self):
        self.assertEqual(convertFahrenheitToKelvin(8.0), 259.817)
    
    def test_fahrenheit_to_celsius_300_should_be(self):
        self.assertEqual(convertFahrenheitToKelvin(300.0), 422.039)

    def test_fahrenheit_to_celsius_1_should_be_255_928(self):
        self.assertEqual(convertFahrenheitToKelvin(1), 255.928)
        
    def test_fahrenheit_to_celsius_8_should_be_259_817(self):
        self.assertEqual(convertFahrenheitToKelvin(8), 259.817)

    def test_fahrenheit_to_celsius_0_should_be_255_372(self):
        self.assertEqual(convertFahrenheitToKelvin(0), 255.372)

    def test_fahrenheit_to_celsius_422_should_be_489_817(self):
        self.assertEqual(convertFahrenheitToKelvin(422), 489.817)