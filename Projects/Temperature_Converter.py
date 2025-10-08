#Make temperature converter calculator

# Constants
FAHRENHEIT_TO_CELSIUS = 5 / 9
CELSIUS_TO_FAHRENHEIT = 9 / 5
OFFSET = 32

# User Inputs
Celsius = 40
Fahrenheit = 25

# Formula for conversion
Convert_to_Fahrenheit = (Celsius * CELSIUS_TO_FAHRENHEIT) + OFFSET
Convert_to_Celsius = (Fahrenheit - OFFSET) * FAHRENHEIT_TO_CELSIUS

# Display

print(f"{Celsius}°C --> {Convert_to_Fahrenheit: .2f}°F")
print(f"{Fahrenheit}°F --> {Convert_to_Celsius: .2f}°C")
