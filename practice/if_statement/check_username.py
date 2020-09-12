current_users = ["Lake", "Tom", "John", "Barco", "Wood"]
new_users = ["Lake", "Wood", "Baku", "Somma", "Gaku"]
for new_user in new_users:
    if new_user.lower().title() in current_users:
        print("Please enter a new username.")
    else:
        print("This username can be use.")
