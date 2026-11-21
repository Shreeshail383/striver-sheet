def print_pattern(n):
    for i in range(n):
        #spaces
        for j in range(n - i + 1):
            print(" ", end=" ")
        #characters
        ch = 'A'
        for j in range(2 * i + 1):
            print(ch, end=" ")
            if j < i:
                ch = chr(ord(ch) + 1)
            else:
                ch = chr(ord(ch) - 1)
        #spaces
        for j in range(n - i - 1):
            print(" ", end=" ")
        print()

t = int(input())
for i in range(t):
    n = int(input())
    print_pattern(n)     