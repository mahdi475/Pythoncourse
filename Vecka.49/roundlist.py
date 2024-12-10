def round_list(lst):
    for i in range(len(lst)):
        lst[i] = round(lst[i], 2)

    return lst

lista = [67.234253, 552009.0001223, 20.3775, 35, 0.732]

print(round_list(lista))