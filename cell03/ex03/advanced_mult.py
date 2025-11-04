table_number = 1

while table_number <= 10:
    
    output_line = f"Table de {table_number}: "
    
    multiplier = 1
    
    while multiplier <= 10:
      
        result = table_number * multiplier
       
        output_line += f"{result} "
        
        multiplier += 1
     
    print(output_line)
   
    table_number += 1