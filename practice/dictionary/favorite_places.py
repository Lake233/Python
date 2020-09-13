favorite_places = {
    "zy" : ["tj", "cd", "tokyo"],
    "lzn" : ["tj", "hb"],
    "zyx" : ["tj"]
    }
for name, places in favorite_places.items():
    if len(places) == 1:
        print(name.title() + "'s favorite place is: " + places[0])
    else:
        print(name.title() + "'s favorite places are:")
        for place in places:
            print(place)