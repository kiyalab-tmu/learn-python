if __name__=="__main__":
    list1=['a','b','c','d','e']
    list2=list(range(5))
    print(list1[0])
    print(list1[4])
    temp=[list1[1],list1[2],list1[3]]
    print(temp)
    list1.extend('f')
    print(list1)
    list1.extend(list2)
    print(list1)
