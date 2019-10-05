def convertCelsiustoKelvin(celsius):
    """
    °C + 273.15 = K
    """
    return celsius + 273.15


def convertCelsiusToFahrenheit(celsius):
    """
    (°C × 9/5) + 32 = °F
    """
    return (celsius * 9 / 5) + 32


def convertFahrenheitToCelsius(fahrenheit):
    """
    (°F − 32) × 5/9 = °C
    """
    return (fahrenheit - 32) * (5 / 9)

def convertFahrenheitToKelvin(fahrenheit):
    """
    (°F − 32) × 5/9 + 273.15 = K
    """
    return round((fahrenheit - 32) * (5 / 9) + 273.15, 3)

def convertKelvinToFahrenheit(kelvin):
    """
    (K − 273.15) × 9/5 + 32 = °F
    """
    return round((kelvin - 273.15) * (9 / 5) + 32, 2) 

def convertKelvinToCelsius(kelvin):
    """
    K − 273.15 = °C
    """
    return round(kelvin - 273.15, 2)