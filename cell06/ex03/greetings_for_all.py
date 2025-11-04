def greetings(name="Noble stranger"):
   
    try:
        float(name)
        
        print("Error: It was not a name.")
        
    except ValueError:
      
        print(f"Hello, {str(name)}!")

greetings("Alexandre")

greetings("Wil")

greetings()

greetings(42)

greetings("42")