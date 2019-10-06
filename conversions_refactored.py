
class ConversionNotPossible(Exception):
    pass

def convert(fromUnit, toUnit, value):
    """
    The main convert function that takes care of the conversion by unit measurement.

    The convert function houses two measurement dicts: temperature & length
    within each respective dict are the relative conversions. The conversion 
    happens through a two step dict k:v lookup. 

    temp -> celsius -> conversion lambda
    temp -> fahrenheit -> conversion lambda
    temp -> kelvin -> conversion lambda


    length -> meters -> conversion lambda
    length -> miles -> conversion lambda
    length -> yards -> conversion lambda

    Args:
        fromUnit(str): A unit of measurement.
        toUnit(str):   A unit of measurement.
        value(float):  The measurement value for conversion.

    Returns:
        A conversion float or an Exception if there's a type mismatch

    """
    
    from_unit = fromUnit.lower()
    to_unit = toUnit.lower()

    temperature_dict = {
        'celsius': {
            'kelvin': lambda celsius: celsius + 273.15,
            'fahrenheit': lambda celsius: (celsius * 9 / 5) + 32,
            'celsius': lambda celsius: float(celsius) 
        },
        'fahrenheit': {
            'kelvin': lambda fahrenheit: round((fahrenheit - 32) * (5 / 9) + 273.15, 3),
            'celsius': lambda fahrenheit: round((fahrenheit - 32) * (5 / 9), 4),
            'fahrenheit': lambda fahrenheit: float(fahrenheit) 
        },
        'kelvin':  {
            'celsius': lambda kelvin: round(kelvin - 273.15, 2),
            'fahrenheit': lambda kelvin: round((kelvin - 273.15) * (9 / 5) + 32, 2),
            'kelvin': lambda kelvin: float(kelvin) 
        },
    }

    length_dict = {
        'meters': {
          'miles': lambda meter: meter / 1609.344,
          'yards': lambda meter: meter * 1.094,
          'meters': lambda meters: float(meters)  
        },
        'miles': {
            'meters': lambda miles: miles * 1609.344,
            'yards': lambda miles: miles * 1760,
            'miles': lambda miles: float(miles)  
        },
        'yards': {
            'meters': lambda yards: yards / 1.094,
            'miles': lambda yards: yards / 1760,
            'yards': lambda yards: float(yards)  
        }

    }

    unit_type = temperature_dict if from_unit in temperature_dict else length_dict

    if to_unit not in unit_type:
        exception_string = f'A Conversion Exception Occured with: {str((from_unit, to_unit))}'

        raise ConversionNotPossible(exception_string)
    else:
        return unit_type[from_unit][to_unit](value) 
