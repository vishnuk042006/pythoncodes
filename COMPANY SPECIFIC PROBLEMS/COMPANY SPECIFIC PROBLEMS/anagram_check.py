# Q11. Anagram Check
from collections import Counter

def is_anagram(a, b):
    return Counter(a) == Counter(b)

if __name__ == "__main__":
    A = input("Enter first string: ")
    B = input("Enter second string: ")
    print("YES" if is_anagram(A, B) else "NO")
