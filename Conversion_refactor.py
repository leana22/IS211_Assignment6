import Conversion

def convert(fromUnit, toUnit, value):
    if fromUnit=="C" and toUnit == "K":
        result = Conversion.convertCelsiusToKelvin(value)
        return result

    elif fromUnit=="C" and toUnit == "F":
        result = Conversion.convertCelsiusToFahrenheit(value)
        return result

    elif fromUnit=="F" and toUnit == "C":
        result = Conversion.convertFahrenheitToCelsius(value)
        return result

    elif fromUnit=="F" and toUnit == "K":
        result = Conversion.convertFahrenheitToKelvin(value)
        return result

    elif fromUnit=="K" and toUnit == "C":
        result = Conversion.convertKelvinToCelsius(value)
        return result

    elif fromUnit=="K" and toUnit == "F":
        result = Conversion.convertKelvinToFahrenheit(value)
        return result

    elif fromUnit=="Me" and toUnit == "Y":
        result = Conversion.convertMeterToYard(value)
        return result

    elif fromUnit=="Me" and toUnit == "Mi":
        result = Conversion.convertMeterToMiles(value)
        return result

    elif fromUnit=="Y" and toUnit == "Me":
        result = Conversion.convertYardToMeter(value)
        return result

    elif fromUnit=="Y" and toUnit == "Mi":
        result = Conversion.convertYardToMiles(value)
        return result

    elif fromUnit=="Mi" and toUnit == "Y":
        result = Conversion.convertMilesToYard(value)
        return result

    elif fromUnit=="Mi" and toUnit == "Me":
        result = Conversion.convertMilesToMeter(value)
        return result
    else:
        print("Conversion was not possible")