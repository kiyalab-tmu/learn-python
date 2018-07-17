
import copy

def quicksort(list_):
    sorted_list = copy.copy(list_)
    recursive_quicksort(sorted_list, 0, len(sorted_list))
    return sorted_list


def recursive_quicksort(list_, start, stop):
    if stop - start == 2:
        if list_[stop-1] < list_[start]:
            list_[start], list_[stop-1] = list_[stop-1], list_[start]
        return
    elif stop - start <= 1:
        return

    med_idx = (start + stop - 1) // 2
    pivot = list_[med_idx]
    i = start
    j = stop - 1
    print((start, stop))
    while True:
        print("list: {0}, (i, j, pivot): {1}".format(list_, (i, j, pivot)))
        while list_[i] < pivot:
            i += 1
        while list_[j] > pivot:
            j -= 1

        if i >= j:
            break
        else:
            list_[i], list_[j] = list_[j], list_[i]

        i += 1
        j -= 1

    recursive_quicksort(list_, start, i-1)
    recursive_quicksort(list_, j+1, stop)

    return


if __name__ == "__main__":
    list1 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(quicksort(list1))
    print(quicksort(list1) == sorted(list1))

    list1 = [1, 1, 1, 1, 0, 0, 0, 0]
    print(quicksort(list1))
    print(quicksort(list1) == sorted(list1))

    list1 = [-1, 0, 1e-10, float("inf"), -float("inf")]
    print(quicksort(list1))
    print(quicksort(list1) == sorted(list1))

    list1 = [1]
    print(quicksort(list1))
    print(quicksort(list1) == sorted(list1))

    list1 = []
    print(quicksort(list1))
    print(quicksort(list1) == sorted(list1))
