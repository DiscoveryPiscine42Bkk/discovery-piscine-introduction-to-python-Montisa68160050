import sys

def shrink(input_string):

    print(input_string[:8]) 

def enlarge(input_string):
    
    num_to_add = 8 - len(input_string)
    
    result = input_string + ('Z' * num_to_add)

    print(result)

parameters = sys.argv[1:]

if len(parameters) < 1:
    print("none")
else:
    for param in parameters:
        param_length = len(param)
        
        if param_length > 8:
            shrink(param)
            
        elif param_length < 8:
            enlarge(param)
            
        else:
            print(param)