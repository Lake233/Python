age = input("Please enter your age: ")
while int(age) > 0:
    if int(age) < 3:
        print("The ticket is free.")
    elif int(age) <= 12:
        print("The price of ticket is 10 dollars.")
    else:
        print("The price of ticket is 15 dollars.")
    age = input("Please enter your age: ")
print("Sorry, it's a wrong age.")