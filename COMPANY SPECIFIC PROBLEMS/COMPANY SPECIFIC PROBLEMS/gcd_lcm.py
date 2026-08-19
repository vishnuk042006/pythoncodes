
import math

def gcd_lcm(a, b):
    g = math.gcd(a, b)
    return g, a * b // g

if __name__ == "__main__":
    A, B = map(int, input("Enter A and B: ").split())
    g, l = gcd_lcm(A, B)
    print(g)
    print(l)
