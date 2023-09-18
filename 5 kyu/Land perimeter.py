def land_perimeter(matrix):
    perimeter = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'X':
                # Check top neighbor
                if i == 0 or matrix[i-1][j] == 'O':
                    perimeter += 1
                # Check bottom neighbor
                if i == len(matrix)-1 or matrix[i+1][j] == 'O':
                    perimeter += 1
                # Check left neighbor
                if j == 0 or matrix[i][j-1] == 'O':
                    perimeter += 1
                # Check right neighbor
                if j == len(matrix[i])-1 or matrix[i][j+1] == 'O':
                    perimeter += 1
    return f"Total land perimeter: {perimeter}"

# Test Cases

print(land_perimeter(
    ['XOOXO',
        'XOOXO',
        'OOOXO',
        'XXOXO',
        'OXOOO']))

print(land_perimeter(
    ['XOOO',
        'XOXO',
        'XOXO',
        'OOXX',
        'OOOO']))
