def fizz_buzz(num):
  if num % 3 != 0 and num % 5 != 0:
    print(num, end="")
  if num % 3 == 0:
    print("Fizz", end="")
  if num % 5 == 0:
    print("Buzz", end="")
  print()

if __name__ == "__main__":
  for i in range(1, 99):
    fizz_buzz(i)
