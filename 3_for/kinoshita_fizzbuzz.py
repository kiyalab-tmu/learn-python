def fizz_buzz(num):
  if num % 3 != 0 and num % 5 != 0:
    print(num, end="")
  if num % 3 == 0:
    print("Fizz", end="")
  if num % 5 == 0:
    print("Buzz", end="")
  print()

if __name__ == "__main__":
    fizz_buzz(1)
    fizz_buzz(3)
    fizz_buzz(15)
    fizz_buzz(25)
