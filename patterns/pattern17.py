def print_pattern(n):
    for i in range(n):
        ch = 'E'
        for j in range(ord(ch) - i, ord(ch) + 1):
            print(chr(j), end=" ")
        print()

t = int(input())
for i in range(t):
    n = int(input())
    print_pattern(n)
