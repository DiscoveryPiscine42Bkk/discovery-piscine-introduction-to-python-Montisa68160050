import math

try:
    user_number = float(input("Give me a number: "))
    
    rounded_up_number = math.ceil(user_number)
    
    print(int(rounded_up_number))
    
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")