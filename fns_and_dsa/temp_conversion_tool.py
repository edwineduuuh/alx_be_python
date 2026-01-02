# Requirements:
# Define Global Conversion Factors:
# At the top of your script, define two global variables 
# FAHRENHEIT_TO_CELSIUS_FACTOR and CELSIUS_TO_FAHRENHEIT_FACTOR to store the 
# conversion factors (e.g., (5/9) for F to C and (9/5) for C to F, respectively).
# Implement Conversion Functions:
# Write a function convert_to_celsius(fahrenheit) that takes a temperature in 
# Fahrenheit and returns the temperature converted to Celsius.
# Write a function convert_to_fahrenheit(celsius) that takes a temperature in 
# Celsius and returns the temperature converted to Fahrenheit.
# Inside each function, use the respective global conversion factor to perform the 
# conversion.
# User Interaction:
# Prompt the user to enter a temperature and specify whether it’s in Celsius or Fahrenheit.
# Based on the user’s input, call the appropriate conversion function and display 
# the converted temperature.
# If gthe user entered a wrong input,raise an error “Invalid temperature. 
# Please enter a numeric value.”
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5 

def convert_to_fahrenheit(celsius):
    fahrenheit =  celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def main():
    print("Temp conversion program")

    temp_input = input("Enter the temperature to convert: ").strip()

    try:
        temperature = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'C':
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature:.1f}°C is {converted:.1f}°F ")  
    elif unit == 'F':
        converted = convert_to_celsius(temperature)
        print(f"{temperature:.1f}°F is {converted:.1f}°C")
    else:
        print("Invalid temperature input")

if __name__ == "__main__":
    main()