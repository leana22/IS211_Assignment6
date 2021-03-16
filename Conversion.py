def convertCelsiusToKelvin(celsius):
    kelvin = round((celsius + 273.15),2)
    return kelvin

def convertCelsiusToFahrenheit(celsius):
    Fahrenheit = round((celsius * 9/5) + 32,2)
    return Fahrenheit

def convertFahrenheitToCelsius(Fahrenheit):
    Celsius = round((Fahrenheit - 32) * 5/9,2)
    return Celsius

def convertFahrenheitToKelvin(Fahrenheit):
    Kelvin = round((Fahrenheit + 459.67) * 5 / 9, 2)
    return Kelvin

def convertKelvinToCelsius(kelvin):
    Celsius = round((kelvin - 273.15),2)
    return Celsius

def convertKelvinToFahrenheit(kelvin):
    Fahrenheit = round((kelvin * 9/5) - 459.67,2)
    return Fahrenheit

def convertMeterToYard(Meter):
    Yard = round(Meter * 1.093613,2)
    return Yard

def convertMeterToMiles(Meter):
    Miles = round(Meter / 1609.344,2)
    return Miles

def convertYardToMeter(Yard):
    Meter = round(Yard / 1.093613,2)
    return Meter

def convertYardToMiles(Yard):
    Miles = round(Yard / 1760, 2)
    return Miles

def convertMilesToYard(Miles):
    Yard = round(Miles * 1760,2)
    return Yard

def convertMilesToMeter(Miles):
    Meter = round(Miles * 1609.344,2)
    return Meter
