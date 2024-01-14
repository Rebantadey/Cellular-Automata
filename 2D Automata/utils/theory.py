def rule(value, array, i, j):
    if array[i, j] == 1 and (value > 3 or value < 2):
        return 0
    elif array[i, j] == 0 and value == 3:
        return 1
    else:
        return array[i, j]
    
def calc_neighbors(array, i, j):
    num_neighbors = array[i-1:i+2, j-1:j+2].sum() - array[i, j]
    return num_neighbors
    
def calc_state(array):
    new_array = array.copy()
    for i in range(0, array.shape[0]):
        for j in range(0, array.shape[1]):
            if i == 0 or i == array.shape[0]-1 or j == 0 or j == array.shape[1]-1:
                new_array[i, j] = 0
            else:
                num_neighbors = calc_neighbors(array, i, j)
                new_array[i, j] = rule(num_neighbors, array, i, j)
    return new_array