# Q9. Element Frequency Analysis
from collections import Counter

def freq_analysis(A):
    freq = Counter(A)
    rep = sum(1 for v in freq.values() if v > 1)
    norep = sum(1 for v in freq.values() if v == 1)
    return rep, norep

if __name__ == "__main__":
    N = int(input("Enter N: "))
    A = list(map(int, input("Enter array: ").split()))
    rep, norep = freq_analysis(A)
    print(rep, norep)
