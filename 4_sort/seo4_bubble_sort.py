def bubble_sort(listseo):
  length = int(len(listseo));
  for j in range(length-1):
    i = j
    for i in range(length-j-1):
      if(listseo[i]>listseo[i+1]):
        temp = listseo[i]
        listseo[i] = listseo[i+1]
        listseo[i+1] = temp
  print(listseo)

if __name__ == '__main__':
    listseo = [6.3, 5.4, 5.5, 1.0,2.2,3]
    bubble_sort(listseo)
