import unittest
from Task4_TemperatureConverter import celsius_to_fahrenheit, fahrenheit_to_celsius

class TestTemperatureConverter(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32.0)
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212.0)
        self.assertAlmostEqual(celsius_to_fahrenheit(-40), -40.0)
        self.assertAlmostEqual(celsius_to_fahrenheit(37), 98.6)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0.0)
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100.0)
        self.assertAlmostEqual(fahrenheit_to_celsius(-40), -40.0)
        self.assertAlmostEqual(fahrenheit_to_celsius(98.6), 37.0)

if __name__ == "__main__":
    unittest.main()
