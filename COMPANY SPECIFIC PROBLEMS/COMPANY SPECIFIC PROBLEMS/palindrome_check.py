
def is_palindrome(s):
    clean = "".join(c.lower() for c in s if c.isalnum())
    return clean == clean[::-1]

if __name__ == "__main__":
    S = input("Enter string: ")
    print(is_palindrome(S))
