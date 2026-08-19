# Q20. String Compression (Run-Length Encoding)
def compress(s):
    result = []
    i = 0
    n = len(s)
    while i < n:
        c = s[i]
        cnt = 0
        while i < n and s[i] == c:
            cnt += 1
            i += 1
        result.append(c + (str(cnt) if cnt > 1 else ''))
    return ''.join(result)

if __name__ == "__main__":
    S = input("Enter string: ")
    print(compress(S))
