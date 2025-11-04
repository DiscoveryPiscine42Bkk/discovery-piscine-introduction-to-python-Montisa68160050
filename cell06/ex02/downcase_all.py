import sys

def downcase_it(input_string):
    return input_string.lower()

parameters = sys.argv[1:]

if not parameters:
    print("none")
else:
    for param in parameters:

        lowercased_param = downcase_it(param)
       
        print(lowercased_param)