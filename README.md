### The tests.py file is responsible for running the tests located at the `/tests` directory 
### To run the tests use the following command:
### `python3 tests.py`

### The reason behind coding the test suite in this manner is to increase the verbosity of the test results.
### The outcome can be done in a simpler way using `nose` but wanted to experiement with `unittest`.

## OUTPUT format for tests in this repo: 

```bash
test_celsius_to_fahrenheit_with_192_should_be_377_6 (test_celsius.TestCelsius) ... ok
test_celsius_to_fahrenheit_with_22_6_should_be_72_68 (test_celsius.TestCelsius) ... ok
test_celsius_to_fahrenheit_with_300_should_be_572 (test_celsius.TestCelsius) ... ok
test_celsius_to_fahrenheit_with_5_should_be_41 (test_celsius.TestCelsius) ... ok
test_celsius_to_fahrenheit_with_88_should_be_191_3 (test_celsius.TestCelsius) ... ok
test_celsius_to_kelvin_with_1030_should_be_1303_15 (test_celsius.TestCelsius) ... ok
test_celsius_to_kelvin_with_10_should_be_283_15 (test_celsius.TestCelsius) ... ok
test_celsius_to_kelvin_with_300_should_be_573_15 (test_celsius.TestCelsius) ... ok
test_celsius_to_kelvin_with_35_should_be_308_15 (test_celsius.TestCelsius) ... ok
test_celsius_to_kelvin_with_5_should_be_278_15 (test_celsius.TestCelsius) ... ok
test_celsius_conversion_five (test_conversions_refactored.TestConvert) ... ok
test_celsius_conversion_four (test_conversions_refactored.TestConvert) ... ok
test_celsius_conversion_one (test_conversions_refactored.TestConvert) ... ok
test_celsius_conversion_three (test_conversions_refactored.TestConvert) ... ok
test_celsius_conversion_two (test_conversions_refactored.TestConvert) ... ok
test_celsius_to_itself (test_conversions_refactored.TestConvert) ... ok
test_celsius_to_kelvin_then_kelvin_to_celsius (test_conversions_refactored.TestConvert) ... ok
test_fahrenheit_conversion_five (test_conversions_refactored.TestConvert) ... ok
test_fahrenheit_conversion_four (test_conversions_refactored.TestConvert) ... ok
test_fahrenheit_conversion_one (test_conversions_refactored.TestConvert) ... ok
test_fahrenheit_conversion_three (test_conversions_refactored.TestConvert) ... ok
test_fahrenheit_conversion_two (test_conversions_refactored.TestConvert) ... ok
test_fahrenheit_to_celsius_then_celsius_to_fahrenheit (test_conversions_refactored.TestConvert) ... ok
test_fahrenheit_to_itself (test_conversions_refactored.TestConvert) ... ok
test_kelvin_conversion_five (test_conversions_refactored.TestConvert) ... ok
test_kelvin_conversion_four (test_conversions_refactored.TestConvert) ... ok
test_kelvin_conversion_one (test_conversions_refactored.TestConvert) ... ok
test_kelvin_conversion_three (test_conversions_refactored.TestConvert) ... ok
test_kelvin_conversion_two (test_conversions_refactored.TestConvert) ... ok
test_kelvin_to_fahrenheit_then_fahrenheit_to_kelvin (test_conversions_refactored.TestConvert) ... ok
test_kelvin_to_itself (test_conversions_refactored.TestConvert) ... ok
test_length_to_temperature_exception_meters_scenario_1 (test_conversions_refactored.TestConvert) ... ok
test_length_to_temperature_exception_meters_scenario_2 (test_conversions_refactored.TestConvert) ... ok
test_length_to_temperature_exception_meters_scenario_3 (test_conversions_refactored.TestConvert) ... ok
test_length_to_temperature_exception_miles_scenario_1 (test_conversions_refactored.TestConvert) ... ok
test_length_to_temperature_exception_miles_scenario_2 (test_conversions_refactored.TestConvert) ... ok
test_length_to_temperature_exception_miles_scenario_3 (test_conversions_refactored.TestConvert) ... ok
test_length_to_temperature_exception_yards_scenario_1 (test_conversions_refactored.TestConvert) ... ok
test_length_to_temperature_exception_yards_scenario_2 (test_conversions_refactored.TestConvert) ... ok
test_length_to_temperature_exception_yards_scenario_3 (test_conversions_refactored.TestConvert) ... ok
test_meters_conversion_five (test_conversions_refactored.TestConvert) ... ok
test_meters_conversion_four (test_conversions_refactored.TestConvert) ... ok
test_meters_conversion_one (test_conversions_refactored.TestConvert) ... ok
test_meters_conversion_three (test_conversions_refactored.TestConvert) ... ok
test_meters_conversion_two (test_conversions_refactored.TestConvert) ... ok
test_meters_to_itself (test_conversions_refactored.TestConvert) ... ok
test_meters_to_miles_then_miles_to_meters (test_conversions_refactored.TestConvert) ... ok
test_meters_to_yards_then_yards_to_meters (test_conversions_refactored.TestConvert) ... ok
test_miles_conversion_five (test_conversions_refactored.TestConvert) ... ok
test_miles_conversion_four (test_conversions_refactored.TestConvert) ... ok
test_miles_conversion_one (test_conversions_refactored.TestConvert) ... ok
test_miles_conversion_three (test_conversions_refactored.TestConvert) ... ok
test_miles_conversion_two (test_conversions_refactored.TestConvert) ... ok
test_miles_to_itself (test_conversions_refactored.TestConvert) ... ok
test_miles_to_yards_then_yards_to_miles (test_conversions_refactored.TestConvert) ... ok
test_temperature_to_length_exception_celsius_kelvin_scenario_1 (test_conversions_refactored.TestConvert) ... ok
test_temperature_to_length_exception_celsius_scenario_1 (test_conversions_refactored.TestConvert) ... ok
test_temperature_to_length_exception_celsius_scenario_2 (test_conversions_refactored.TestConvert) ... ok
test_temperature_to_length_exception_celsius_scenario_3 (test_conversions_refactored.TestConvert) ... ok
test_temperature_to_length_exception_fahrenheit_scenario_1 (test_conversions_refactored.TestConvert) ... ok
test_temperature_to_length_exception_fahrenheit_scenario_2 (test_conversions_refactored.TestConvert) ... ok
test_temperature_to_length_exception_fahrenheit_scenario_3 (test_conversions_refactored.TestConvert) ... ok
test_temperature_to_length_exception_kelvin_scenario_2 (test_conversions_refactored.TestConvert) ... ok
test_temperature_to_length_exception_kelvin_scenario_3 (test_conversions_refactored.TestConvert) ... ok
test_yards_conversion_five (test_conversions_refactored.TestConvert) ... ok
test_yards_conversion_four (test_conversions_refactored.TestConvert) ... ok
test_yards_conversion_one (test_conversions_refactored.TestConvert) ... ok
test_yards_conversion_three (test_conversions_refactored.TestConvert) ... ok
test_yards_conversion_two (test_conversions_refactored.TestConvert) ... ok
test_yards_to_itself (test_conversions_refactored.TestConvert) ... ok
test_fahrenheit_to_celsius_0_should_be_255_372 (test_fahrenheit.TestFahrenheit) ... ok
test_fahrenheit_to_celsius_1_should_be_255_928 (test_fahrenheit.TestFahrenheit) ... ok
test_fahrenheit_to_celsius_300_should_be (test_fahrenheit.TestFahrenheit) ... ok
test_fahrenheit_to_celsius_422_should_be_489_817 (test_fahrenheit.TestFahrenheit) ... ok
test_fahrenheit_to_celsius_8_should_be_259_817 (test_fahrenheit.TestFahrenheit) ... ok
test_fahrenheit_to_kelvin_with_0_should_be_255_372 (test_fahrenheit.TestFahrenheit) ... ok
test_fahrenheit_to_kelvin_with_300_should_be_422_039 (test_fahrenheit.TestFahrenheit) ... ok
test_fahrenheit_to_kelvin_with_422_should_be_489_817 (test_fahrenheit.TestFahrenheit) ... ok
test_fahrenheit_to_kelvin_with_5_should_be_258_15 (test_fahrenheit.TestFahrenheit) ... ok
test_fahrenheit_to_kelvin_with_8_should_be_259_817 (test_fahrenheit.TestFahrenheit) ... ok
test_kelvin_to_celsius_with_1_should_be_neg_272_15 (test_kelvin.TestKelvin) ... ok
test_kelvin_to_celsius_with_273_15_should_be_0 (test_kelvin.TestKelvin) ... ok
test_kelvin_to_celsius_with_300_should_be_26_85 (test_kelvin.TestKelvin) ... ok
test_kelvin_to_celsius_with_370_15_should_be_97 (test_kelvin.TestKelvin) ... ok
test_kelvin_to_celsius_with_380_should_be_106_85 (test_kelvin.TestKelvin) ... ok
test_kelvin_to_fahrenheit_with_1_should_be_neg_457_87 (test_kelvin.TestKelvin) ... ok
test_kelvin_to_fahrenheit_with_273_15_should_be_32 (test_kelvin.TestKelvin) ... ok
test_kelvin_to_fahrenheit_with_300_should_be_80_33 (test_kelvin.TestKelvin) ... ok
test_kelvin_to_fahrenheit_with_370_15_should_be_206_6 (test_kelvin.TestKelvin) ... ok
test_kelvin_to_fahrenheit_with_380_should_be_224_33 (test_kelvin.TestKelvin) ... ok

----------------------------------------------------------------------
Ran 90 tests in 0.005s

OK

```