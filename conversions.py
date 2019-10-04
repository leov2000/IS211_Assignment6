from fractions import Fraction

def convertCelsiustoKelvin(celsius):
    """
    °C + 273.15 = K
    """
    return celsius + 273.15


def convertCelsiusToFahrenheit(celsius):
    """
    (°C × 9/5) + 32 = °F
    """
    f_frac = Fraction(9, 5)
    conversion = (celsius * f_frac) + 32

    return float(conversion) if float(conversion) % 1 != 0 else int(conversion) 

