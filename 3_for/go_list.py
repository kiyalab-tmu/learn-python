list1 = ["a", "b", "c", "d", "e"]
print(list1[0])
print(list1[4])
print(list1[1:4])
list1.append("f")
print(list1)

list2 = list(range(5))
list1.extend(list2)
print(list1)