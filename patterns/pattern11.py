def print_pattern(n):
    space = 2 * (n - 1)
    for i in range(n):
        #numbers
        for j in range(1, i + 1):
            print(j, end=" ")
        #spaces
        for j in range(1, space + 1):
            print(" ", end=" ")
        #numbers
        for j in range(i, 0, -1):
            print(j, end=" ")
        print() 
        space -= 2

t = int(input())
for i in range(t):
    n = int(input())
    print_pattern(n)
