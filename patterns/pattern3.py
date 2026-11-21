def print_pattern(n):
    for i in range(n):
        for j in range(i + 1):
            print(j + 1, end=" ")
        print()

t = int(input())
for i in range(t):
    n = int(input())
    print_pattern(n)     