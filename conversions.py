def convertCelsiustoKelvin(celsius):
    """
    A conversion function used to convert celsius to kelvin
    using this formula:  °C + 273.15 = K

    Args:
        celsius(float)
    
    Returns:
        A converted kelvin value.
    """
    return celsius + 273.15

def convertCelsiusToFahrenheit(celsius):
    """
    A conversion function used to convert celsius to fahrenheit
    using this formula: (°C × 9/5) + 32 = °F

    Args:
        celsius(float)
    
    Returns:
        A converted fahrenheit value.
    """
    return (celsius * 9 / 5) + 32


def convertFahrenheitToCelsius(fahrenheit):
    """
    A conversion function used to convert fahrenheit to celsius
    using this formula: (°F − 32) × 5/9 = °C

    Args:
        fahrenheit(float)
    
    Returns:
        A converted celsius value.
    """
    return round((fahrenheit - 32) * (5 / 9), 4)

def convertFahrenheitToKelvin(fahrenheit):
    """
    A conversion function that converts fahrenheit to kelvin
    using this formula: (°F − 32) × 5/9 + 273.15 = K

    Args:
        fahrenheit(float)
    
    Returns:
        A converted kelvin value.
    """
    return round((fahrenheit - 32) * (5 / 9) + 273.15, 3)

def convertKelvinToFahrenheit(kelvin):
    """
    A conversion function that converts kelvin to fahrenheit
    using this formula: (K − 273.15) × 9/5 + 32 = °F

    Args:
        kelvin(float)
    
    Returns:
        A converted fahrenheit value.
    """
    return round((kelvin - 273.15) * (9 / 5) + 32, 2) 

def convertKelvinToCelsius(kelvin):
    """
    A conversion function that converts kelvin to celsius
    using this formula: K − 273.15 = °C

    Args:
        kelvin(float)

    Returns:
        A converted celsius value. 
    """
    return round(kelvin - 273.15, 2)