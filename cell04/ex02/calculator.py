try:
   
    num1 = int(input("Give me the first number: "))
   
    num2 = int(input("Give me the second number: "))
    
    print("Thank you!")
    
    addition = num1 + num2
    print(f"{num1} + {num2} = {addition}")
    
    subtraction = num1 - num2
    print(f"{num1} - {num2} = {subtraction}")
    
    multiplication = num1 * num2
    print(f"{num1} * {num2} = {multiplication}")
   
    if num2 != 0:
        division = num1 / num2 
        print(f"{num1} / {num2} = {division:.2f}") 
    else:
        print(f"{num1} / {num2} = Cannot divide by zero.")

except ValueError:
    print("Error: Invalid input. Please enter only integers.")