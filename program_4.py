#Program (partially) Written By: Ainsley Bellamy
#Date Written: 01/27/2025
#Program Title: Fahrenheit_to_Celsius

def temp_conversion(celsius):
    fahrenheit = 0.0
#calculation from celsius to fahrenheit
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit
if __name__ == '__main__':
    celsius = 0.0
    fahrenheit = 0.0
# Get the Celsius temperature.
    celsius = float(input("Enter a Celsius temperature: "))
    fahrenheit = temp_conversion(celsius)
# Display the Fahrenheit temperature.
    print ("That is equal to", format(fahrenheit, '.2f'), "degrees Fahrenheit.")

#Question--Why not write it like this?

# def temp_conversion():
#     celsius = float(input("Enter a Celsius temperature: "))
#     fahrenheit = (9/5) * celsius + 32
#     print ("That is equal to", format(fahrenheit, '.2f'), "degrees Fahrenheit.")
# temp_conversion()

