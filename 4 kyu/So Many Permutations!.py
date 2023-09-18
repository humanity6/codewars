import itertools

def permutations(s):
    p = itertools.permutations(s)
    mylist = []
    for i in p:
        mylist.append("".join(i))
    return list(set(mylist))

print(permutations('aabb'))
print(permutations('a'))