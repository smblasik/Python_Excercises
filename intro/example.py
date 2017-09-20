import datetime

filename=datetime.datetime.now()


def create_file():
    #This file creates an empty file
    with open(filename.strftime("%Y-%m-%d"+".txt"),"w") as file:
        file.write("") # write an empty string

create_file()
