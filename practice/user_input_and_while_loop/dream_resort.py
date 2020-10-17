response = {}
polling_active = True
while polling_active:
    name = input("What's your name? ")
    answer = input("If you could visit one place in the world, where would you go? ")
    response[name] = answer
    repeat = input("Would you like to let another people respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
print("\n---Poll Results---")
for name, answer in response.items():
    print(name + " would like to go to the " + answer + ".")
