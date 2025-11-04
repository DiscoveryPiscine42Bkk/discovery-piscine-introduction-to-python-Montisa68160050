try:
    multiplier = int(input("Enter a number: "))
    
    for i in range(1, 11):
        result = multiplier * i
        
        print(f"{multiplier} x {i} = {result}")

except ValueError:
    print("Error: Invalid input. Please enter an integer.")