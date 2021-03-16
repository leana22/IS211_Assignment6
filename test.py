import unittest
import Conversion
import Conversion_refactor

class Tests(unittest.TestCase):

    def test_celsius_to_kelvin(self):
        celsius= 183
        expected = 456.15
        actual = Conversion.convertCelsiusToKelvin(celsius)
        self.assertEqual(actual, expected, "Celsius to kelvin conversion failed")

    def test_celsius_to_fahrenheit(self):
        celsius = 183
        expected = 361.4
        actual = Conversion.convertCelsiusToFahrenheit(celsius)
        self.assertEqual(actual, expected, "Celsius to fahrenheit conversion failed")

    def test_fahrenheit_to_celsius(self):
        Fahrenheit = 85
        expected = 29.44
        actual = Conversion.convertFahrenheitToCelsius(Fahrenheit)
        self.assertEqual(actual, expected, "Fahrenheit to celsius conversion failed")

    def test_fahrenheit_to_kelvin(self):
        Fahrenheit = 85
        expected = 302.59
        actual = Conversion.convertFahrenheitToKelvin(Fahrenheit)
        self.assertEqual(actual, expected, "Fahrenheit to Kelvin conversion failed")

    def test_kelvin_to_celsius(self):
        Kelvin = 365
        expected = 91.85
        actual = Conversion.convertKelvinToCelsius(Kelvin)
        self.assertEqual(actual, expected, "Kelvin to celsius conversion failed")

    def test_kelvin_to_fahrenheit(self):
        Kelvin = 365
        expected = 197.33
        actual = Conversion.convertKelvinToFahrenheit(Kelvin)
        self.assertEqual(actual, expected, "Kelvin to fahrenheit conversion failed")

    def test_convert(self):
        fromUnit = "C"
        toUnit = "K"
        value = 183
        expected = 456.15
        actual = Conversion.convertCelsiusToKelvin(fromUnit, toUnit, value)
        self.assertEqual(actual, expected, "Celsius to kelvin conversion failed")

        fromUnit = "C"
        toUnit = "F"
        value = 183
        expected = 361.4
        actual = Conversion.convertCelsiusToFahrenheit(fromUnit, toUnit, value)
        self.assertEqual(actual, expected, "Celsius to fahrenheit conversion failed")

        fromUnit = "F"
        toUnit = "C"
        value = 85
        expected = 29.44
        actual = Conversion.convertFahrenheitToCelsius(fromUnit, toUnit, value)
        self.assertEqual(actual, expected, "Fahrenheit to celsius conversion failed")

        fromUnit = "F"
        toUnit = "K"
        value = 85
        expected = 302.59
        actual = Conversion.convertFahrenheitToKelvin(fromUnit, toUnit, value)
        self.assertEqual(actual, expected, "Fahrenheit to Kelvin conversion failed")

        fromUnit = "K"
        toUnit = "C"
        value = 365
        expected = 91.85
        actual = Conversion.convertKelvinToCelsius(fromUnit, toUnit, value)
        self.assertEqual(actual, expected, "Kelvin to celsius conversion failed")

        fromUnit = "K"
        toUnit = "F"
        value = 365
        expected = 197.33
        actual = Conversion.convertKelvinToFahrenheit(fromUnit, toUnit, value)
        self.assertEqual(actual, expected, "Kelvin to fahrenheit conversion failed")

        fromUnit = "Me"
        toUnit = "Y"
        value = 200
        expected = 218.72
        actual = Conversion_refactor.convert(fromUnit, toUnit, value)
        self.assertEqual(actual, expected, "Celsius to kelvin conversion failed")

        fromUnit = "Me"
        toUnit = "Mi"
        value = 200
        expected = 0.12
        actual = Conversion_refactor.convert(fromUnit, toUnit, value)
        self.assertEqual(actual, expected, "Celsius to kelvin conversion failed")

        fromUnit = "Y"
        toUnit = "Me"
        value = 200
        expected = 18.88
        actual = Conversion_refactor.convert(fromUnit, toUnit, value)
        self.assertEqual(actual, expected, "Celsius to kelvin conversion failed")

        fromUnit = "Y"
        toUnit = "Mi"
        value = 200
        expected = 0.11
        actual = Conversion_refactor.convert(fromUnit, toUnit, value)
        self.assertEqual(actual, expected, "Celsius to kelvin conversion failed")

        fromUnit = "Mi"
        toUnit = "Y"
        value = 200
        expected = 352000
        actual = Conversion_refactor.convert(fromUnit, toUnit, value)
        self.assertEqual(actual, expected, "Celsius to kelvin conversion failed")

        fromUnit = "Mi"
        toUnit = "Me"
        value = 200
        expected = 321868.80
        actual = Conversion_refactor.convert(fromUnit, toUnit, value)
        self.assertEqual(actual, expected, "Celsius to kelvin conversion failed")

if __name__ == "__main__":
    unittest.main()