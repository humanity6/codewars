def generate_hashtag(s="abc"):
    if len(s) == 0:
        return False
    mylist = s.split(" ")
    templist = []
    for word in mylist:
        templist.append(word.title())
    s = " ".join(templist).replace(" ","")
    s = "#" + s
    if len(s) > 140:
        return False
    return s

print(generate_hashtag(" Hello there thanks for trying my Kata"))