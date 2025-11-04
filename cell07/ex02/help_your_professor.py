def average(class_data):
   
    if not class_data:
        return 0.0 

    total_score = 0
    num_students = 0
    
    for score in class_data.values():
        total_score += score
        num_students += 1
    
    class_average = float(total_score) / num_students
   
    return class_average

class_2D = {
    "jean": 18,
    "luc": 15,
    "zoe": 8
}

class_3C = {
    "quentin": 17,
    "marie": 10,
    "muriel": 16,
    "stephanie": 13,
    "stephanie": 18, 
    "alexis": 13
}

avg_2D = average(class_2D)
print(f"Average for class 2D: {avg_2D:.2f}") 

avg_3C = average(class_3C)
print(f"Average for class 3C: {avg_3C:.2f}")