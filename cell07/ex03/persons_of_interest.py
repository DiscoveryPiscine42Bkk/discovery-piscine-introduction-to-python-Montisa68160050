from datetime import datetime

def famous_births(persone):
   
    sorted_persone = sorted(
        persone.items(), 
        key=lambda item: item[1]['date_of_birth']
    )

    for _, person_data in sorted_persone:
        name = person_data['name']
        date_of_birth = person_data['date_of_birth']
   
        print(f"{name} was born in {date_of_birth}.")


women_scientists = {
    "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
    "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
    "gros": {"name": "Gros Supporter", "date_of_birth": "1906"}
}

famous_births(women_scientists)