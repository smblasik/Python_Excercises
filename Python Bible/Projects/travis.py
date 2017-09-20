title_bar = "="*30
print(title_bar)
print("  Travis the Security Robot")
print(title_bar)
print()

# Know Users
known_users = ["Alice","Bob","Charlie","Dan","Emma","Fred","Georgie","Harry"]

while True:
    print('Hi! My name is Travis')                              # Travis introduces himself
    name = input("What is your name? ").strip().capitalize()    # Input from user # Strips and capitalizes name

    # Program detects known users
    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed (y/n)? ").lower()
        if remove == "y":
            known_users.remove(name)
    # If a user is not recongized they can be added to the list
    else:
        add = input("I'm sorry. I don't recognize you. Would you like to be added (y/n)?").lower()
        if add == "y":
            known_users.append(name)
            print("Welcome {}!".format(name))
    print()
