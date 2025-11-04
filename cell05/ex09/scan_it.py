import sys

import re 

parameters = sys.argv[1:]
param_count = len(parameters)

if param_count != 2:
    print("none")
else:
    keyword = parameters[0]
    search_string = parameters[1]
    
    if keyword not in search_string:
        print("none")
    else:
        
        found_matches = re.findall(keyword, search_string)
        count = len(found_matches)
      
        print(count)