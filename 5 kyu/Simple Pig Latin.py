def pig_it(text):
    new_name = ""
    temp = text.split(" ")
    for word in temp:
        if not word.isalnum():
            new_name = new_name + " " + word
        else:
            new_name_temp = word[1:] + word[0] + "ay"
            new_name = new_name + " " + new_name_temp
    return new_name.lstrip()

print(pig_it('Pig latin is cool'))