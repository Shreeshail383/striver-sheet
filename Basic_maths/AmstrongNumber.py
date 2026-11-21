def amstrong_number(n):
    rev = 0
    dup = n
    sum = 0
    while n > 0:
        lastdigit = n % 10
        sum = sum + (lastdigit ** 3)
        n = n // 10
    rev = rev * 10 + lastdigit
    if sum == dup:
        print("Amstrong Number")
    else:
        print("Not Amstrong Number")

n = 371
amstrong_number(n)