original_array = [2, 8, 9, 40, 8, 22, -12, 2]

new_array = []

for number in original_array:
    if number > 5:
        new_number = number + 2
 
        new_array.append(new_number)

print("Original array:", original_array)
print("New array:", new_array)