
class ConversionNotPossible(Exception):
    pass

def convert(fromUnit, toUnit, value):
    from_unit = fromUnit.lower()
    to_unit = toUnit.lower()

    temperature_dict = {
        'celsius': {
            'kelvin': lambda celsius: celsius + 273.15,
            'fahrenheit': lambda celsius: (celsius * 9 / 5) + 32,
            'celsius': lambda identity: identity 
        },
        'fahrenheit': {
            'kelvin': lambda fahrenheit: round((fahrenheit - 32) * (5 / 9) + 273.15, 3),
            'celsius': lambda fahrenheit: (fahrenheit - 32) * (5 / 9),
            'fahrenheit': lambda identity: identity 
        },
        'kelvin':  {
            'celsius': lambda kelvin: round(kelvin - 273.15, 2),
            'fahrenheit': lambda kelvin: round((kelvin - 273.15) * (9 / 5) + 32, 2),
            'kelvin': lambda identity: identity 
        },
    }

    length_dict = {
        'meters': {
          'miles': lambda meter: meter / 1609.344,
          'yards': lambda meter: meter * 1.094,
          'meters': lambda identity: identity 
        },
        'miles': {
            'meters': lambda miles: miles * 1609.344,
            'yards': lambda miles: miles * 1760,
            'miles': lambda identity: identity 
        },
        'yards': {
            'meters': lambda yards: yards / 1.094,
            'miles': lambda yards: yards / 1760,
            'yards': lambda identity: identity 
        }

    }

    unit_type = temperature_dict if from_unit in temperature_dict else length_dict

    if to_unit not in unit_type:
        exception_string = f'A Conversion Exception Occured with: {str((from_unit, to_unit))}'

        raise ConversionNotPossible(exception_string)
    else:
        print(unit_type[from_unit][to_unit](value)) 


if __name__ == '__main__':
    convert('fahrenheit', 'kelvin', 100)
    convert('meters', 'fahrenheit', 1)
