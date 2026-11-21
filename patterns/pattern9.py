def print_pattern(n):
    for i in range(1, 2*n):
        star = i
        if i > n:
            star = 2*n-i
        for j in range(1, star+1):
            print("*", end=" ")
        print()

t = int(input())
for i in range(t):
    n = int(input())
    print_pattern(n)     