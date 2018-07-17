def Fibonacci_Yield_tool(n):
    a, b = 0, 1
    while n > 0:
        yield b
        a, b = b, a + b
        n -= 1



def fibonacci(n):
    # return [f for i, f in enumerate(Fibonacci_Yield_tool(n))]
    return list(Fibonacci_Yield_tool(n))

if __name__ == '__main__':
    num = input("Please input a num:")
    num = fibonacci(int(num))
    print(num)
