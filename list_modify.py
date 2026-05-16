def put(value, lst):
    for i in range(len(lst)):
        if lst[i] == "":
            lst[i] = value
            return i
    return -1

def remove(value, lst):
    borrados = 0
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == value:
            lst[i] = ""
            borrados += 1
    return borrados
