def print_pattern(n):
    for i in range(n):
        for j in range(n - i - 1):
            ch = chr(ord('A') + j)
            print(ch, end=" ")
        print()

t = int(input())            
for i in range(t):
    n = int(input())
    print_pattern(n)