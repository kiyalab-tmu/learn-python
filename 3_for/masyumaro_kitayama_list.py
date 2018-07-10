list1 = ["a", "b", "c", "d", "e"];
print(list1[0]);
print(list1[4]);
print("%c %c %c"%(list1[1], list1[2], list1[3]));
list1.append("f");
print(list1);

list2 = list(range(5));
list1 = list1 + list2;
print(list1);
