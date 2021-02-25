import math
def isPrime2(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    m = int(math.sqrt(n)) + 1
    for i in range(3, m, 2):
        if m % i == 0:
            return False
    return True

def isPrime3(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    m = n // 2 + 1
    for i in  range(3, m, 2):
        for i in range(3, m, 2):
            if m % i == 0:
                return False
    return True


def isPrime(n):
    if n < 2:
        return False
    prime = True
    # m = n // 2 + 1
    # for i in  range(3, m, 2)
    for i in range(2, n):
        if n % i == 0:
            print(n, "is divisible by", i)
            prime = False
        return prime

while True:
  number =  input("Enter an integer number ( Enter 0 to exit): ")
  number = int(number)
  if number == 0:
      break
  prime = isPrime(number)
  if prime is True:
      print(number, " is prime number")
  else:
      print(number, " is not a prime number")