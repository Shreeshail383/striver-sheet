def print_pattern(n):
    for i in range(n):
        ch = chr(ord('A') + i)
        for j in range(i + 1):
            print(ch, end=" ")
        print()

t = int(input())
for i in range(t):
    n = int(input())
    print_pattern(n)