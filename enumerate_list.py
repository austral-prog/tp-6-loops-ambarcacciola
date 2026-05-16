def enumerate_list(lst):
    lista = []
    index = 0
    for elemento in lst:
        if elemento != "":
            lista.append(f"{index}. {elemento}")
            index += 1
    return lista


def enumerate_backwards(lst):
    lista = []
    index = 0
    for elemento in lst:
        if elemento != "":
            backwards = elemento[::-1]
            lista.append(f"{index}. {backwards}")
            index += 1
    return lista
