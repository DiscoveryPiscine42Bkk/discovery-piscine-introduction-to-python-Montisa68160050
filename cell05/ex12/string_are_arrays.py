import sys

if len(sys.argv) != 2:
    print("None")
else:
    input_string = sys.argv[1]
   
    a_count = input_string.count('a')
    
    
    if a_count == 0:
        print("The character 'a' is not found in this string")
    else:
        print(("The character 'a' is found in this string\n" * a_count).strip())