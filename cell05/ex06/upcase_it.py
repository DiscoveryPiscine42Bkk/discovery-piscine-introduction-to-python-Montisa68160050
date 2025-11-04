import sys

if len(sys.argv) != 2:
    print("none")
else:
    input_string = sys.argv[1]
    
    uppercased_string = input_string.upper()
    
    print(uppercased_string)