title_bar = "="*21
print(title_bar)
print("  Hello You Program")
print(title_bar)

# Ask user for Name
name = input("Enter your name: ")

# Ask user for Age
age = input("How old are you: ")

# Ask user for City
city = input("What city do you live in? ")

# Ask user what you enjoy
enjoy = input("What do you enjoy? ")

# Create output text
string = "Your name is {0}. You are {1} years old. You live in {2}. You enjoy {3}."
output = string.format(name,age,city,enjoy)

#Print output to screen
print(output)
