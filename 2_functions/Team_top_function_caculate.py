def Caculate(num1,num2):
    sum = num1 + num2
    difference = num1 - num2
    product = num1*num2
    quotient = num1/num2
    remainder = num1%num2
    
    print(sum)
    print(type(sum))
    print(difference)
    print(type(difference))
    print(product)
    print(type(product))
    print(quotient)
    print(type(quotient))
    print(remainder)
    print(type(remainder))

if __name__  == "__main__":
    temp1=input("Please insert number1:")
    temp2=input("Please insert number2:")
    print(type(temp1))
    Caculate(int(temp1),int(temp2))
    
    
