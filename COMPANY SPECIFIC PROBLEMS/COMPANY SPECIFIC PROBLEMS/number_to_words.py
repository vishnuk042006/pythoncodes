# Q14. Number to Words (0-999)
ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
        'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
        'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

def convert(n):
    if n == 0:
        return 'Zero'
    elif n < 20:
        return ones[n]
    elif n < 100:
        return tens[n // 10] + (' ' + ones[n % 10] if n % 10 else '')
    else:
        return ones[n // 100] + ' Hundred' + ((' ' + convert(n % 100)) if n % 100 else '')

if __name__ == "__main__":
    N = int(input("Enter N (0-999): "))
    print(convert(N))
