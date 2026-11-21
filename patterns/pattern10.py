def print_pattern(n):
    start = 1
    for i in range(n):
        if i % 2 == 0:
            start = 1
        else:
            start = 0
        for j in range(i + 1):
            print(start, end=" ")
            start = 1 - start
        print()

t = int(input())
for i in range(t):
    n = int(input())
    print_pattern(n)