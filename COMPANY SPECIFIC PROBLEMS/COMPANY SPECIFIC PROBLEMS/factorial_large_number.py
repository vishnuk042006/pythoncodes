# Q12. Factorial of Large Number (print digits)
import math

def factorial_digits(n):
    return list(str(math.factorial(n)))

if __name__ == "__main__":
    N = int(input("Enter N: "))
    for d in factorial_digits(N):
        print(d)
