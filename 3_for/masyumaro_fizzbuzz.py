def fizz_buzz(num):
    if num % 3 == 0:
        if num % 5 == 0:
            print('fizz buzz');
        else:
            print('fizz');
    elif num % 5 == 0:
        print('buzz');
    else:
        print(num);

if __name__ == '__main__':
    for i in range(100):
        fizz_buzz(i + 1);
