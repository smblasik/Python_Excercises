# Variable Scope

a = 100

def f1():
    print(a)

def f2():
    print(a)

f1()
f2()
