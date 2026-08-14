# Q1. Gym Exercise - Minimum Exercises to Get Tired
def min_exercises(E, A):
    A = sorted(A, reverse=True)
    total = count = 0
    for x in A:
        for _ in range(2):
            total += x
            count += 1
            if total >= E:
                return count
    return -1

if __name__ == "__main__":
    E, N = map(int, input("Enter E and N: ").split())
    A = list(map(int, input("Enter N energy values: ").split()))
    print(min_exercises(E, A))
