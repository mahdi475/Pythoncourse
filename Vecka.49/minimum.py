def set_min_value(nummrar, minstanummer):
    new_list = []
    for i in range(len(nummrar)):
        if nummrar[i] < minstanummer:
            nummrar[i] = minstanummer
            new_list.append(minstanummer)
        else:
            new_list.append(nummrar[i])
    if new_list == nummrar:
        return nummrar
    else:
        return new_list
    


lst = [30, 58, 51, 46, 29, 59]

print(set_min_value(lst, 24))