import sys

parameters = sys.argv[1:]

if not parameters:
 
    print("none")
else:
    for param in parameters:

        if param.endswith("ism"):

            print(param)
        else:
            print(param + "*ism")