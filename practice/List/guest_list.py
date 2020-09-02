guestList=["chen", "zeng", "liao"]
message="I will invite " + guestList[0].title() + "," + guestList[1].title() + "," + guestList[2].title() + " to have dinner."
print(message)
message2=guestList[0].title() + " can't come to the dinner."
print(message2)
del guestList[0]
guestList.insert(0, "Zhuang")
message3="I will invite " + guestList[0].title() + "," + guestList[1].title() + "," + guestList[2].title() + " to have dinner."
print(message3)
print("I find a bigger dinner table.")
guestList.insert(0, "Xie")
guestList.insert(2, "Tan")
guestList.append("Deng")
message4="I will invite " + guestList[0].title() + "," + guestList[1].title() + "," + guestList[2].title() + \
        "," + guestList[3].title() + "," + guestList[4].title() + "," + guestList[5].title() + " to have dinner."
print(message4)
print("I just can invite two guys to have dinner.")
print("Sorry " + guestList.pop().title() + ", I can't invite you.")
print("Sorry " + guestList.pop().title() + ", I can't invite you.")
print("Sorry " + guestList.pop().title() + ", I can't invite you.")
print("Sorry " + guestList.pop().title() + ", I can't invite you.")
print(guestList[0].title() + ", you are invited by me.")
print(guestList[1].title() + ", you are invited by me.")
del guestList[0]
del guestList[0]
print(guestList)