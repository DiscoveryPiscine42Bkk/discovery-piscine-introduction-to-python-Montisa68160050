user_input = ""

while user_input != "STOP":
    user_input = input("What you gotta say? ")
    if user_input == "STOP":
        print("I got that: STOP")
    else:
        print(f"I got that: {user_input}")

print("I got that anything else? STOP")