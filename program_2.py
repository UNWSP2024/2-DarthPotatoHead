#Program Written By: Ainsley Bellamy
#Date Written: 01/27/2025
#Program Title: getAverage

def average_age():
    # Get User Input
    friend1 = int(input("Enter your age: "))
    friend2 = int(input("Enter your age: "))
    friend3 = int(input("Enter your age: "))
    friend4 = int(input("Enter your age: "))
    friend5 = int(input("Enter your age: "))

    # Sum ages and average ages
    sumAges = ((friend1 + friend2 + friend3 + friend4 + friend5)/5)

    # Print the results
    print(f'The Average Age is: {sumAges:.2f}')

# Line which calls the above function.
average_age()