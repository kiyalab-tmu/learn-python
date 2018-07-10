def fizz_buzz(num):
  if num % 3 != 0 and num % 5 != 0
    print(num, end="")
  if num % 3 == 0:
    print("Fizz", end="")
  if num % 5 == 0:
    print("Buzz", end="")
  print()

if __name__ == "__main__":
    # execute only if run as a script
    fizz_buzz(2)
