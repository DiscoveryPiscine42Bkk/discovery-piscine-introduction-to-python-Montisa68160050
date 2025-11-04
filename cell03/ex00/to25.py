try:
    start_number = int(input("Enter a number less than 25: "))
    if start_number > 25:
        print("Error")
    else:
        for current_number in range(start_number, 26):
            print(f"Inside the loop, my variable is {current_number}")

except ValueError:
    print("Error: Invalid input. Please enter an integer.")