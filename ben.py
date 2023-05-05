def is_border(i, row_length, j, col_length): 
    if i == 0 or i == row_length or j == 0 or j == col_length: 
        return True
    return False 


def is_outside_matrix(i, j, matrix): 
    if i < 0 or j < 0 or i > len(matrix)-1 or j > len(matrix[0])-1: 
        return True
    return False


def border_islands_key(i, j):
    return '{}{}'.format(i, j)


def rec(i, j, matrix, border_islands):
    steps = [
            (0, 1),
            (1, 0),
            (0, -1), 
            (-1, 0)
            ]
    for [ix, jx] in steps: 
        new_i = ix + i
        new_j = jx + j 
        if is_outside_matrix(new_i, new_j, matrix): 
            continue
        neigh = matrix[new_i][new_j]
        key = border_islands_key(new_i, new_j)
        if neigh == 1 and not( key in border_islands) : 
            border_islands[key] = True 
            rec(new_i, new_j, matrix, border_islands)


def removeIsland(matrix): 
    # 1 -> black 
    # 0 -> white 
    # true means its a 1 and its an edge 
    # '00' -> true 
    # '01' -> false 
    # key -> [] 
    # index -> '00'
    # 30 -> [31, 40]
    border_islands = {}
    
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == 1 and is_border(i, len(matrix)-1, j, len(row)-1): 
                if border_islands_key(i, j) in border_islands:
                    continue
                border_islands[border_islands_key(i, j)] = True
                rec(i, j, matrix, border_islands)
    
    for i, row in enumerate(matrix): 
        for j, value in enumerate(row): 
            if value == 1 and not(border_islands_key(i,j) in border_islands):
                matrix[i][j] = 0
    
    return matrix 


if __name__ == '__main__':
    matrix=[ 
            [1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 1, 0],
            [1, 1, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 1],
           ]

    rIsland = removeIsland(matrix)
    for row in rIsland:
        print(row)
