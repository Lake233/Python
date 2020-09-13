cities = {
    "Tianjin" : {
        "country" : "China",
        "population" : "15million",
        "fact" : "It has a football team."
        },
    "Tokyo" : {
        "country" : "Japan",
        "population" : "14million",
        "fact" : "Small area, large population."
        },
    "New York" : {
        "country" : "US",
        "population" : "8million",
        "fact" : "They have red bull."
        }
    }
for name, content in cities.items():
    print(name + "'s informations: ")
    print("\tCountry: " + content["country"])
    print("\tPopulation: " + content["population"])
    print("\tFact: " + content["fact"] + "\n")

