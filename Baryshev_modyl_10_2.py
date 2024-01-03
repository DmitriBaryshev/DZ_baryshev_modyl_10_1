# Задание 2
class TemperatureConverter:
    count = 0

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        TemperatureConverter.count += 1
        return celsius * 9/5 + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        TemperatureConverter.count += 1
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def get_conversion_count():
        return TemperatureConverter.count


print(TemperatureConverter.celsius_to_fahrenheit(25))
print(TemperatureConverter.fahrenheit_to_celsius(77))
print(TemperatureConverter.get_conversion_count())


# Задание 3
class LengthConverter:
    @staticmethod
    def meters_to_yards(meters):
        return meters * 1.09361

    @staticmethod
    def yards_to_meters(yards):
        return yards / 1.09361


print(LengthConverter.meters_to_yards(10))
print(LengthConverter.yards_to_meters(10))
