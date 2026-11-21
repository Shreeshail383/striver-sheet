def LargestDigit(n):
    largestdigit = 0
    while n > 0:
        lastdigit = n % 10
        if lastdigit > largestdigit:
            largestdigit = lastdigit
        n = n // 10
    return largestdigit

n  = 54692
print(LargestDigit(n))