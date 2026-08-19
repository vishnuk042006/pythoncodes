# Q25. String Cutting into Maximum Equal Pieces
from collections import Counter
from math import gcd
from functools import reduce

def max_equal_pieces(s):
    freq = Counter(s)
    return reduce(gcd, freq.values())

if __name__ == "__main__":
    S = input("Enter string: ").strip()
    print(max_equal_pieces(S))
