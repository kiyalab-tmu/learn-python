def bubble(list_x):
    length = len(list_x)
    for i in range(length):
        for j in range(length-i):
            if list_x[i] > list_x[i+j]:
                list_x[i], list_x[i+j] = list_x[i+j], list_x[i]


if __name__ == "__main__":
    listY = [1, 1, 1, -1, 0, 0, 0]
    bubble(listY)
    print(listY)
