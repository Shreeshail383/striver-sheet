def print_pattern(n):
    for i in range(n):
        #spaces
        for j in range(n - i + 1):
            print(" ", end=" ")
        #stars
        for j in range(2 * i + 1):
            print("*", end=" ")
        #spaces
        for j in range(n - i - 1):
            print(" ", end=" ")
        print()

t = int(input())
for i in range(t):
    n = int(input())
    print_pattern(n)     