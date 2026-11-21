def palindrome(n):
    if n < 0 or (n % 10 == 0 and n != 0):
        return False
    rev = 0
    original = n
    while n > rev:
        rev = rev * 10 + n % 10
        n //= 10
    return original if n == rev or n == rev // 10 else False

n = 12321
print(palindrome(n))
