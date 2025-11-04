original_array = [2, 8, 9, 40, 8, 22, -12, 2]

temp_array = []

for number in original_array:
    if number > 5:
        new_number = number + 2
       
        temp_array.append(new_number)

unique_set = set(temp_array)

new_array = list(unique_set)

print("Original array:", original_array)
print("New array:", new_array)