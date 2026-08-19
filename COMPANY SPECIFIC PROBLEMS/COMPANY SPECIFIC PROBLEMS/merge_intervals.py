# Q30. Merge Intervals
def merge_intervals(ivs):
    ivs = sorted(ivs)
    merged = [list(ivs[0])]
    for s, e in ivs[1:]:
        if s <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], e)
        else:
            merged.append([s, e])
    return merged

if __name__ == "__main__":
    N = int(input("Enter N: "))
    ivs = [list(map(int, input().split())) for _ in range(N)]
    result = merge_intervals(ivs)
    print(*[f'[{a},{b}]' for a, b in result])
