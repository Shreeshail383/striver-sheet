def print_pattern(n):
    num = 1
    for i in range(n):
        for j in range(i + 1):
            print(num, end=" ")
            num += 1
        print()

t = int(input())
for i in range(t):  
    n = int(input())
    print_pattern(n)