title_bar = "="*30
print(title_bar)
print("    Pig Latin Translator")
print(title_bar)

while True:
    #get sentence form user
    original = input("Enter setence to translate: ").strip().lower()
    if original == "exit":
        break
    #split sentence into words
    words = original.split()
    #loop through words and convert to pig latin
    new_words = []
    vowel = "aeiou"
    for i in words:
        if i[0] in vowel:
            new_word = i + "yay"
            new_words.append(new_word)
        else:
            vowel_pos = 0
            for letter in i:
                if letter not in vowel:
                    vowel_pos += 1
                else:
                    break
            cons = i[:vowel_pos]
            the_rest = i[vowel_pos:]
            new_word = the_rest + cons + "ay"
            new_words.append(new_word)


    #stick words back together
    output=" ".join(new_words)

    #output the final string
    print(output.capitalize())
