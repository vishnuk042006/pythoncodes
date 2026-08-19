
def count_vc(s):
    v = c = 0
    for ch in s:
        if ch.isalpha():
            if ch.lower() in 'aeiou':
                v += 1
            else:
                c += 1
    return v, c

if __name__ == "__main__":
    S = input("Enter string: ")
    v, c = count_vc(S)
    print(v, c)
