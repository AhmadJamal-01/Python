
# Prompt the user for a temperature in Fahrenheit
fahrenheit = float(input("Enter temperature in Fahrenheit: "))  # Casting input to float

# Convert Fahrenheit to Celsius
celsius = (fahrenheit - 32) * 5.0 / 9.0

# Output the temperature converted to Celsius
print(f"Temperature: {fahrenheit}F = {celsius}C")
