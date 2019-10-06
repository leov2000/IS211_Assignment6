import os
import sys
import unittest

module_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(module_dir, '../'))

from conversions_refactored import convert, ConversionNotPossible

class TestConvert(unittest.TestCase):
    """Convert Tests"""

    @classmethod
    def setUpClass(cls):
        cls.kelvin = 'kelvin'
        cls.fahrenheit = 'fahrenheit'
        cls.celsius = 'celsius'
        cls.meters = 'meters'
        cls.miles = 'miles'
        cls.yards = 'yards' 

    def test_kelvin_to_fahrenheit_then_fahrenheit_to_kelvin(self):
        value = 22.0
        kelvin_to_fahrenheit = convert(self.kelvin, self.fahrenheit, value)
        self.assertEqual(convert(self.fahrenheit, self.kelvin, kelvin_to_fahrenheit), value)

    def test_celsius_to_kelvin_then_kelvin_to_celsius(self):
        value = 273.15
        celsius_to_kelvin = convert(self.celsius, self.kelvin, value)
        self.assertEqual(convert(self.kelvin, self.celsius, celsius_to_kelvin), value)
    
    def test_fahrenheit_to_celsius_then_celsius_to_fahrenheit(self):
        value = 78.0
        fahrenheit_to_celsius = convert(self.fahrenheit, self.celsius, value)
        self.assertEqual(convert(self.celsius, self.fahrenheit, fahrenheit_to_celsius), value)

    def test_meters_to_miles_then_miles_to_meters(self):
        value = 1.0
        meters_to_miles = convert(self.meters, self.miles, value)
        self.assertEqual(convert(self.miles, self.meters, meters_to_miles), value)
    
    def test_miles_to_yards_then_yards_to_miles(self):
        value = 2.0
        miles_to_yards = convert(self.miles, self.yards, value)
        self.assertEqual(convert(self.yards, self.miles, miles_to_yards), value)
    
    def test_meters_to_yards_then_yards_to_meters(self):
        value = 3.0 
        meters_to_yards = convert(self.meters, self.yards, value)
        self.assertEqual(convert(self.yards, self.meters, meters_to_yards), value)

    def test_meters_to_itself(self):
         self.assertEqual(convert(self.meters, self.meters, 3.0), 3.0)    
    
    def test_miles_to_itself(self):
        self.assertEqual(convert(self.miles, self.miles, 222.0), 222.0)
    
    def test_yards_to_itself(self):
        self.assertEqual(convert(self.yards, self.yards, 88.0), 88.0)

    def test_kelvin_to_itself(self):
        self.assertEqual(convert(self.kelvin, self.kelvin, 55.0), 55.0) 

    def test_fahrenheit_to_itself(self):
        self.assertEqual(convert(self.fahrenheit, self.fahrenheit, 8888.0), 8888.0)

    def test_celsius_to_itself(self):
        self.assertEqual(convert(self.celsius, self.celsius, 555.0), 555.0)
    
    def test_temperature_to_length_exception_celsius_scenario_1(self):
        self.assertRaises(ConversionNotPossible, convert, self.celsius, self.miles, 5)

    def test_temperature_to_length_exception_celsius_scenario_2(self):
        self.assertRaises(ConversionNotPossible, convert, self.celsius, self.meters, 15)

    def test_temperature_to_length_exception_celsius_scenario_3(self):
        self.assertRaises(ConversionNotPossible, convert, self.celsius, self.yards, 5)

    def test_temperature_to_length_exception_fahrenheit_scenario_1(self):
        self.assertRaises(ConversionNotPossible, convert, self.fahrenheit, self.miles, 15)

    def test_temperature_to_length_exception_fahrenheit_scenario_2(self):
        self.assertRaises(ConversionNotPossible, convert, self.fahrenheit, self.meters, 5)

    def test_temperature_to_length_exception_fahrenheit_scenario_3(self):
        self.assertRaises(ConversionNotPossible, convert, self.fahrenheit, self.yards, 15)

    def test_temperature_to_length_exception_celsius_kelvin_scenario_1(self):
        self.assertRaises(ConversionNotPossible, convert, self.kelvin, self.miles, 5)

    def test_temperature_to_length_exception_kelvin_scenario_2(self):
        self.assertRaises(ConversionNotPossible, convert, self.kelvin, self.meters, 15)

    def test_temperature_to_length_exception_kelvin_scenario_3(self):
        self.assertRaises(ConversionNotPossible, convert, self.kelvin, self.yards, 5)

    def test_length_to_temperature_exception_meters_scenario_1(self):
        self.assertRaises(ConversionNotPossible, convert, self.meters, self.celsius, 15)

    def test_length_to_temperature_exception_meters_scenario_2(self):
        self.assertRaises(ConversionNotPossible, convert, self.meters, self.fahrenheit, 5)

    def test_length_to_temperature_exception_meters_scenario_3(self):
        self.assertRaises(ConversionNotPossible, convert, self.meters, self.kelvin, 15)

    def test_length_to_temperature_exception_miles_scenario_1(self):
        self.assertRaises(ConversionNotPossible, convert, self.miles, self.celsius, 5)

    def test_length_to_temperature_exception_miles_scenario_2(self):
        self.assertRaises(ConversionNotPossible, convert, self.miles, self.fahrenheit, 15)

    def test_length_to_temperature_exception_miles_scenario_3(self):
        self.assertRaises(ConversionNotPossible, convert, self.miles, self.kelvin, 5)

    def test_length_to_temperature_exception_yards_scenario_1(self):
        self.assertRaises(ConversionNotPossible, convert, self.yards, self.celsius, 15)

    def test_length_to_temperature_exception_yards_scenario_2(self):
        self.assertRaises(ConversionNotPossible, convert, self.yards, self.fahrenheit, 5)

    def test_length_to_temperature_exception_yards_scenario_3(self):
        self.assertRaises(ConversionNotPossible, convert, self.yards, self.kelvin, 15)