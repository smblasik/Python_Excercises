title_bar = "="*30
print(title_bar)
print("    Cinema Simulator")
print(title_bar)

films = {
    "Finding Dory":[3,5],
    "Bourne":[18,5],
    "Tarzan":[15,5],
    "Ghost Busters":[12,5]
    }

while True:
    choice = input("What movie do you want to see? ").strip().title()
    if choice in films:
        age = int(input("How old are you? ").strip())

        #Check user age
        if age >= films[choice][0]:

            #Check number seats
            if films[choice][1] > 0:
                print("Enjoy the film")
                films[choice][1] -= 1
                print(films[choice][1])
            else:
                print("Sorry we are sold out")
        else:
            print("You are too young to see that film")

    else:
        print("We dont have that film...")
