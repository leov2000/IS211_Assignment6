from fractions import Fraction
from decimal import getcontext, Decimal

def convertCelsiustoKelvin(celsius):
    """
    °C + 273.15 = K
    """
    return celsius + 273.15


def convertCelsiusToFahrenheit(celsius):
    """
    (°C × 9/5) + 32 = °F
    """
    getcontext().prec = 2
    f_frac = Fraction(9, 5)
    conversion = (celsius * f_frac) + 32
    return float(conversion) if float(conversion) % 1 != 0 else int(conversion) 

def convertFahrenheitToCelsius(fahrenheit):
    """
    (°F − 32) × 5/9 = °C
    """
    pass

def convertFahrenheitToKelvin(fahrenheit):
    """
    (°F − 32) × 5/9 + 273.15 = K
    """
    pass 

def convertKelvinToFahrenheit(kelvin):
    """
    (K − 273.15) × 9/5 + 32 = °F
    """
    pass

def convertKelvinToCelsius(kelvin):
    """
    K − 273.15 = °C
    """
    pass 