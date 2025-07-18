FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR= 9/5
def c_f(c): 
    """Converts temperature from Celsius to Fahrenheit."""
    return(c*CELSIUS_TO_FAHRENHEIT_FACTOR) +32
def f_c(f):
    """Converts temperature from Fahrenheit to Celsius."""
    return(f-32)*FAHRENHEIT_TO_CELSIUS_FACTOR

while True:
    try:
       temp_to_convert=int(input("Enter the temperature to convert:"))
       break    
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

    

temp_units=input("Is this temperature in Celsius or Fahrenheit? (C/F):").lower()
if temp_units=="c":
    print(c_f(temp_to_convert))
elif temp_units=="f":
    print(f_c(temp_to_convert))
else:
    print("Wrong input,choose either C of F")    

