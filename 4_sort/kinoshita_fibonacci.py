def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n < 0:
        raise ValueError("n must be a natural number")

    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    for i in range(20):
        print("n: {0}, Fn: {1}".format(i, fibonacci(i)))
