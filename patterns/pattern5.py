def print_pattern(n):
    for i in range(1, n):
        for j in range(n - i + 1):
            print("*", end=" ")
        print()

t = int(input())
for i in range(t):
    n = int(input())
    print_pattern(n)     