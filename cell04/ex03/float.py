try:
    user_input = input("Give me a number: ")
   
    if '.' in user_input:
        print("This number is a decimal.")
        
    else:
        number = int(user_input)
        print("This number is an integer.")
        
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")