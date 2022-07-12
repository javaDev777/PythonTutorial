vowels = 0
consonants = 0

for letter in "supercalifragilisticeexpialidocious":
    if letter.lower() in "aeiou":
        vowels = vowels + 1
    elif letter == "":
        pass
    else:
        consonants = consonants + 1

print("There are {} vowels".format(vowels))
print("There are () consonants".format(consonants))

students ={
    "male":["Tom","Charle","Harry","Frank"],
    "female":["Sarah","Huda", "Samantha","Emily","Elizabeth"]
    }
for key in students.keys():
    for name in students[key]:
        if "s" in name:
            print(name)


