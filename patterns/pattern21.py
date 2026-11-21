def print_pattern(n):
    for i in range(2 * n - 1):
        for j in range(2 * n - 1):
            top = i
            left = j
            right = 2 * n - 2 - j
            down = 2 * n - 2 - i
            print(n - min(min(top, down), min(left, right)), end=" ")
        print()

t = int(input("Enter the number of test cases: "))
for _ in range(t):
    n = int(input("Enter the value of n: "))
    print_pattern(n)

    