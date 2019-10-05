import os
import sys
import unittest

module_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(module_dir, '../'))

from conversions import convertKelvinToCelsius, convertKelvinToFahrenheit

class TestKelvin(unittest.TestCase):
    """Kelvin Conversion Tests"""

    def test_kelvin_to_celsius_with_300_should_be_26_85(self):
        self.assertEqual(convertKelvinToCelsius(300.0), 26.85)

    def test_kelvin_to_celsius_with_273_15_should_be_0(self):
        self.assertEqual(convertKelvinToCelsius(273.15), 0)

    def test_kelvin_to_celsius_with_370_15_should_be_97(self):
        self.assertEqual(convertKelvinToCelsius(370.15), 97)

    def test_kelvin_to_celsius_with_380_should_be_106_85(self):
        self.assertEqual(convertKelvinToCelsius(380.0), 106.85)

    def test_kelvin_to_celsius_with_1_should_be_neg_272_15(self):
        self.assertEqual(convertKelvinToCelsius(1.0), -272.15)
