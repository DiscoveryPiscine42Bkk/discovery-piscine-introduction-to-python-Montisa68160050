def array_of_names(persone):
   
    full_names_list = []
 
    for first_name, last_name in persone.items():
     
        formatted_first_name = first_name.capitalize()
        formatted_last_name = last_name.capitalize()
        
        full_name = f"{formatted_first_name} {formatted_last_name}"
     
        full_names_list.append(full_name)
       
    return full_names_list

persone = {
    "jean": "valjean",
    "gros": "sOuPPer",
    "Javier": "rEi",
    "fifi": "brindacier"
}

result_array = array_of_names(persone)
print(result_array)