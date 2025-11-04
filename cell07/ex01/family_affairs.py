def find_the_redheads(family):
   
    def is_redhead(name):
        return family[name] == 'red'

    redheads_filter_object = filter(is_redhead, family.keys())
    
    return list(redheads_filter_object)

family_roster = {
    "Florian": "red",
    "Davis": "blue",
    "Virginia": "brunette",
    "Marie": "red",
    "Frank": "red"
}

redheads = find_the_redheads(family_roster)
print(redheads)