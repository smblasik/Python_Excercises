from random import choice

title_bar = "="*30
print(title_bar)
print("    Baby Conversation Simulator")
print(title_bar)

questions = ["Why is the sky blue? ", "Why is there a face on the moon? ","Where are all the dinosaurs? "]
question = choice(questions)

answer = input(question).lower().strip()

while answer != "just because":
    answer = input("Why? ").strip().lower()
    if answer == "exit":
        break

print("Ohh.. Okay")
