travel_log_list = [
    { 
        "country": "sao_tome",
        "cities_visited":['Boa morte', 'Caixao grande', 'Traz cimiterio'],
         "total_visits" : 2 
    },
    { 
        "country": "Portuga",
        "cities_visited":['Nazarem', 'Cascais', 'Porto'], 
        "total_visits" : 3 
    } 
]

for entry in travel_log_list:
    print(entry)
    print(entry['country'])
    print(entry['cities_visited'])
    print(entry['total_visits'])