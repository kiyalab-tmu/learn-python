def Fizz_Buzz(num):
        if num <= 0:
            print(num)
        elif num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
        
if __name__  == "__main__":
    temp = input("Please input a number:\n")
    guess = int(temp)
    for i in range(guess):
        Fizz_Buzz(i)
        
    
