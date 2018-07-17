import copy

def bubble_sort(list_):
    sorted_list = copy.copy(list_)
    for i in range(len(sorted_list)):
        for j in range(i, len(sorted_list)):
            if sorted_list[i] > sorted_list[j]:
                tmp = sorted_list[j]
                sorted_list[j] = sorted_list[i]
                sorted_list[i] = tmp

    return sorted_list

if __name__ == "__main__":
    list1 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(list1)
    print(bubble_sort(list1))
    print(bubble_sort(list1) == sorted(list1))

    list1 = [1, 1, 1, 1, 0, 0, 0, 0]
    print(list1)
    print(bubble_sort(list1))
    print(bubble_sort(list1) == sorted(list1))

    list1 = [-1, 0, 1e-10, float("inf"), -float("inf")]
    print(list1)
    print(bubble_sort(list1))
    print(bubble_sort(list1) == sorted(list1))

    list1 = [1]
    print(list1)
    print(bubble_sort(list1))
    print(bubble_sort(list1) == sorted(list1))

    list1 = []
    print(list1)
    print(bubble_sort(list1))
    print(bubble_sort(list1) == sorted(list1))
