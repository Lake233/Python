pizzas=["Chicago Pizza", "New York-Style Pizza", "Greek Pizza"]
for pizza in pizzas:
    print(pizza)
    print("I like " + pizza)
print("\nI really love pizza!")
friend_pizzas=pizzas[:]
pizzas.append("Cheese Pizza")
friend_pizzas.append("Meat Pizza")
print("My favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are: ")
for friend_pizza in friend_pizzas:
    print(friend_pizza)