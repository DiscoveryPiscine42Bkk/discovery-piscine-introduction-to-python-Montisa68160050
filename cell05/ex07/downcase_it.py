import sys

if len(sys.argv) != 2:
    print("none")
else:
    input_string = sys.argv[1]
    
    lowercased_string = input_string.lower()
    
    print(lowercased_string)