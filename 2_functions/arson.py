def calculate(num1,num2):

    sum = num1 + num2
    sub = num1 - num2
    pro = num1 * num2
    div = num1 / num2
    quo = num1 // num2
    rem = num1 % num2

    print('和：', sum)
    print('差：', sub)
    print('積：', pro)
    print('商：', div)
    print('商の整数部：', quo)
    print('余り：', rem)

if __name__ == '__main__':
    calculate(14,5)
