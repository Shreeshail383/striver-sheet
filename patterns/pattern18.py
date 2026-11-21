def print_pattern(n):
    iniS = 0
    for i in range(n):
        #stars
        for j in range(n - i):
            print("*", end="")
        #spaces
        for j in range(iniS):
            print(" ", end="")
        #stars
        for j in range(n - i):
            print("*", end="")
        iniS += 2
        print()

        
    iniS = 2 * n - 2 #8
    for i in range(1, n + 1):
        #stars
        for j in range(i):
            print("*", end="")
        #spaces
        for j in range(iniS):
            print(" ", end="")
        #stars
        for j in range(i):
            print("*", end="")
        iniS -= 2
        print()

t = int(input("Enter the number of test cases: "))
for _ in range(t):
    n = int(input("Enter the value of n: "))
    print_pattern(n)
