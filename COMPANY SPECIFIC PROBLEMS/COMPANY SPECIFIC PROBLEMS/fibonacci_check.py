# Q3. Fibonacci Number Check
import math

def is_perfect_square(n):
    s = math.isqrt(n)
    return s * s == n

def is_fibonacci(n):
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

if __name__ == "__main__":
    N = int(input("Enter N: "))
    print("YES" if is_fibonacci(N) else "NO")
