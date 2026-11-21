
def lcm(n1, n2):
    n = max(n1, n2)
    i = 1

    while True:
        mult = n * i

        if mult % n1 == 0 and mult % n2 == 0:
            return mult

        i += 1


n1 = 10
n2 = 30

print(lcm(n1, n2))
