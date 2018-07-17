def bubble_sort(list):
    for passnum in range(len(list)-1,0,-1):
        for i in range(passnum):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
    return list


if __name__ == '__main__':
    list = [3,4,1,0.2,2,9,3.5,-1*float("inf"),8,float("inf"),5]
    bubble_sort(list)
    print(list)
