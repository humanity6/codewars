def move_zeros(array):
    for i in array:
        if i == 0:
            array.remove(i) 
            array.append(i) 
    return array

print(move_zeros([1,2,0,1,0,1,0,3,0,1]))