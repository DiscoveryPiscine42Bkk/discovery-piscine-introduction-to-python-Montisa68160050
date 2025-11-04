try:
    current_age = int(input("Please tell us your age: "))
    
    age_in_10 = current_age + 10
    print(f"In 10 years, you'll be {age_in_10} years old.")
    
    age_in_20 = current_age + 20
    print(f"In 20 years, you'll be {age_in_20} years old.")
    
    age_in_30 = current_age + 30
    print(f"In 30 years, you'll be {age_in_30} years old.")

except ValueError:
    print("Error: Invalid input. Please enter a valid integer for your age.")