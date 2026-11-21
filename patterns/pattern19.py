def print_pattern(n):
    spaces = 2 * n - 2
    for i in range(2 * n - 1):
        stars = i
        if i >= n:
            stars = 2 * n - i - 2
        #stars
        for j in range(stars + 1):
            print("*", end="")
        #spaces
        for j in range(spaces):
            print(" ", end="")
        #stars
        for j in range(stars + 1):
            print("*", end="")
        if i < n - 1:
            spaces -= 2
        else:
            spaces += 2
        print()

t = int(input("Enter the number of test cases: "))
for _ in range(t):
    n = int(input("Enter the value of n: "))
    print_pattern(n)