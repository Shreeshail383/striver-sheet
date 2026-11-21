def print_pattern(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0 or j == n - 1 or i == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

t = int(input("Enter the number of test cases: "))
for _ in range(t):
    n = int(input("Enter the value of n: "))
    print_pattern(n)
