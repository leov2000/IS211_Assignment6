import os
import sys
import unittest

module_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(module_dir, '../'))

from conversions_refactored import convert, ConversionNotPossible

class TestConvert(unittest.TestCase):
    """Refactored Conversion Tests

        checks that all temperature conversions are working

        checks that all distance conversions are working 

        check that converting from one unit to itself returns the same value for all units

        checks that converting from incompatible unit types raise a `ConversionNotPossible` exception

    """

    @classmethod
    def setUpClass(cls):
        cls.kelvin = 'kelvin'
        cls.fahrenheit = 'fahrenheit'
        cls.celsius = 'celsius'
        cls.meters = 'meters'
        cls.miles = 'miles'
        cls.yards = 'yards'

    def test_celsius_conversion_one(self):
        self.assertEqual(convert(self.fahrenheit, self.celsius, 78.0), 25.5556)

    def test_celsius_conversion_two(self):
        self.assertEqual(convert(self.fahrenheit, self.celsius, 55.0), 12.7778)

    def test_celsius_conversion_three(self):
        self.assertEqual(convert(self.kelvin, self.celsius, 333.0), 59.85)

    def test_celsius_conversion_four(self):
        self.assertEqual(convert(self.kelvin, self.celsius, -550.0), -823.15)

    def test_celsius_conversion_five(self):
        self.assertEqual(convert(self.fahrenheit, self.celsius, -78.0), -61.1111)

    def test_fahrenheit_conversion_one(self):
        self.assertEqual(convert(self.celsius, self.fahrenheit, 78.0), 172.4)

    def test_fahrenheit_conversion_two(self):
        self.assertEqual(convert(self.celsius, self.fahrenheit, 55.0), 131.0)

    def test_fahrenheit_conversion_three(self):
        self.assertEqual(convert(self.kelvin, self.fahrenheit, 333.0), 139.73)

    def test_fahrenheit_conversion_four(self):
        self.assertEqual(convert(self.kelvin, self.fahrenheit, -550.0), -1449.67)

    def test_fahrenheit_conversion_five(self):
        self.assertEqual(convert(self.celsius, self.fahrenheit, -78.0), -108.4)

    def test_kelvin_conversion_one(self):
        self.assertEqual(convert(self.celsius, self.kelvin, 78.0), 351.15)

    def test_kelvin_conversion_two(self):
        self.assertEqual(convert(self.celsius, self.kelvin, 55.0), 328.15)

    def test_kelvin_conversion_three(self):
        self.assertEqual(convert(self.fahrenheit, self.kelvin, 333.0), 440.372)

    def test_kelvin_conversion_four(self):
        self.assertEqual(convert(self.fahrenheit, self.kelvin, -550.0), -50.183)

    def test_kelvin_conversion_five(self):
        self.assertEqual(convert(self.celsius, self.kelvin, -78.0), 195.14999999999998)

    def test_meters_conversion_one(self):
        self.assertEqual(convert(self.yards, self.meters, 78.0), 71.2979890310786)

    def test_meters_conversion_two(self):
        self.assertEqual(convert(self.yards, self.meters, 55.0), 50.274223034734916)

    def test_meters_conversion_three(self):
        self.assertEqual(convert(self.miles, self.meters, 333.0), 535911.552)

    def test_meters_conversion_four(self):
        self.assertEqual(convert(self.miles, self.meters, -550.0), -885139.2000000001)

    def test_meters_conversion_five(self):
        self.assertEqual(convert(self.yards, self.meters, -78.0), -71.2979890310786)

    def test_miles_conversion_one(self):
        self.assertEqual(convert(self.meters, self.miles, 78.0), 0.04846695299451205)

    def test_miles_conversion_two(self):
        self.assertEqual(convert(self.meters, self.miles, 55.0), 0.03417541557305337)

    def test_miles_conversion_three(self):
        self.assertEqual(convert(self.yards, self.miles, 333.0), 0.18920454545454546)

    def test_miles_conversion_four(self):
        self.assertEqual(convert(self.yards, self.miles, -550.0), -0.3125)

    def test_miles_conversion_five(self):
        self.assertEqual(convert(self.meters, self.miles, -78.0), -0.04846695299451205)

    def test_yards_conversion_one(self):
        self.assertEqual(convert(self.miles, self.yards, 78.0), 137280.0)

    def test_yards_conversion_two(self):
        self.assertEqual(convert(self.miles, self.yards, 55.0), 96800)

    def test_yards_conversion_three(self):
        self.assertEqual(convert(self.meters, self.yards, 333.0), 364.302)

    def test_yards_conversion_four(self):
        self.assertEqual(convert(self.meters, self.yards, -550.0), -601.7)

    def test_yards_conversion_five(self):
        self.assertEqual(convert(self.miles, self.yards, -78.0), -137280.0)        

    def test_kelvin_to_fahrenheit_then_fahrenheit_to_kelvin(self):
        value = 22.0
        kelvin_to_fahrenheit = convert(self.kelvin, self.fahrenheit, value)
        self.assertEqual(convert(self.fahrenheit, self.kelvin, kelvin_to_fahrenheit), value)

    def test_celsius_to_kelvin_then_kelvin_to_celsius(self):
        value = 273.15
        celsius_to_kelvin = convert(self.celsius, self.kelvin, value)
        self.assertEqual(convert(self.kelvin, self.celsius, celsius_to_kelvin), value)
    
    def test_fahrenheit_to_celsius_then_celsius_to_fahrenheit(self):
        value = 12.0
        fahrenheit_to_celsius = convert(self.fahrenheit, self.celsius, value)
        self.assertEqual(round(convert(self.celsius, self.fahrenheit, fahrenheit_to_celsius)), value)

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


