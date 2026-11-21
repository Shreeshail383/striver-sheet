def print_all_divisors(n):
    dividors = [] #[1, 2, 3, 4, 6, 12, 18, 36]
    for i in range(1, int(n**0.5) + 1): #int(n**0.5) + 1 is used to reduce the time complexity from O(n) to O(sqrt(n))
        if n % i == 0:
            dividors.append(i)
            if i != n // i: #to avoid adding the square root twice for perfect squares (6 * 6 = 36) we only want to add 6 once
                dividors.append(n // i)
    return sorted(dividors)

n = 36
print(print_all_divisors(n))