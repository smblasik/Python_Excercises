#Functions
def add(x,y):
    return x + y

print(add(5,10))

def rev(text):
    return text[::-1]

print(rev("Bitch").lower())

def about(name,age,likes = "Python"):
    sentence = "Meet {}! they are {} years old and they like {}.".format(name,age,likes)
    return sentence

def add(*numbers):
    total = 0
    for i in numbers:
        total += i
    return total

print(add(1,2,3,4,5,6,7,8))

dictionary = {"name":"Scott","age":23,"likes":"Python"}
print(about(**dictionary))

def foo(**kwargs):
    for key, value in kwargs.items():
        print("{}:{}".format(key,value))

foo(ziyad="male",sex="male",john="male")
