a = input("Enter Number 1: ")
b = input("Enter Number 2: ")

def divisible(c,d):
    if int(c) % int(d) == 0:
        print("Those numbers are divisible")
    else:
        print("Those numbers are not divisible")

divisible(a,b)
