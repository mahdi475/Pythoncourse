def max_neighbors(lst):
    max_neighbors_tal = lst[0] + lst[1]
    for i in range(len(lst) - 1):
        granne_tal = lst[i] + lst[i + 1]
        if granne_tal > max_neighbors_tal:
            max_neighbors_tal = granne_tal
    return max_neighbors_tal
    



bleh = [-47, -56, -47, -12, -93]
lista = [8, 1, -4, 10, -12, 22, -5]

print(max_neighbors(bleh))
print(max_neighbors(lista))


