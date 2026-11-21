
class Solution:
    def isPrime(self, n):
        if n < 2:
            return False

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False

        return True

    def PrimeUptoN(self, n):
        count = 0

        for i in range(2, n + 1):
            if self.isPrime(i):
                count += 1

        return count


sol = Solution()
n = 11
print(sol.PrimeUptoN(n))
