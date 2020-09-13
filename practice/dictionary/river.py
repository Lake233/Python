rivers = {"nile" : "epypt", "Yangtze river" : "china", "Yellow river" : "china"}
for river,country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")
for river in rivers.keys():
    print(river)
for country in set(rivers.values()):
    print(country)