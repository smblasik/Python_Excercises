# Tuples

(A,B,C) = 1,2,3     # Create multiple variables with tuples
D,E,F = "123"

#Dictionaries

students = {"Alice":25,"Bob":27,"Claire":17,"Dan":21,"Emma":22}
students["Fred"] = 25
students["Alice"] = 26
del students["Fred"]

# Gives the keys in dictionary
list(student.keys())
list(student.values())

students = {
        "Alice":{"id":ID001,"age":26,"grade":"A"},
        "Bob":{"id":ID002,"age":27,"grade":"B"},
        "Claire":{"id":ID003,"age":17,"grade":"C"},
        "Dan":{"id":ID004,"age":21,"grade":"D"},
        "Emma":{"id":ID005,"age":22,"grade":"E"},
        }
studnets["Dan"]["age"]
studentsp["Emma"]["id"],students["Emma"]["grade"]
