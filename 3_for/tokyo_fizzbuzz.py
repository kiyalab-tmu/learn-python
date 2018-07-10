def fizz_buzz(num):

  if num%3==0 and num%5!=0:
    print("Fizz")
  elif num%5==0 and num%3!=0:
    print("Buzz")
  elif num%5==0 and num%3==0:
    print("FizzBuzz")
  else:
    print(num)

if __name__=="__main__":

    for i in range(99):
        fizz_buzz(i+1)
