import sys

parameters = sys.argv[1:]

param_count = len(parameters)

if param_count == 0:
    print("None")
else:
    print(param_count)
    
    if param_count >= 1:
        param1 = parameters[0]
        print(f"{param1}: {len(param1)}")

    if param_count >= 2:
        param2 = parameters[1]
        print(f"{param2}: {len(param2)}")

    if param_count >= 3:
        param3 = parameters[2]
        print(f"{param3}: {len(param3)}")
