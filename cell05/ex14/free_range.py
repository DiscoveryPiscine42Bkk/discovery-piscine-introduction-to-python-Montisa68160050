import sys

parameters = sys.argv[1:]
param_count = len(parameters)

if param_count != 2:
    print("none")
else:
    
    try:
        start_num = int(parameters[0])
 
        stop_num = int(parameters[1])
        
        result_list = list(range(start_num, stop_num))
       
        print(result_list)
        
    except ValueError:
   
        print("none")