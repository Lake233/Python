numbers=[value for value in range(1,11)]
print("The first three items in the list are: ")
for number in numbers[:3]:
    print(number)
print("Three items from the middle of the list are: ")
for number in numbers[3:6]:
    print(number)
print("The last three items in the list are: ")
for number in numbers[-3:]:
    print(number)