# Function to Convert Celcius to Farenheit

def fer(cel):
    if cel > -273.15:
        answer = cel * 1.8 + 32
        return answer


temperatures=[10,-20,-289,100]

for c in temperatures:
    with open("temp.txt","a+") as file:
        if c > -273.15:
            file.write(str(fer(c)) + "\n")
