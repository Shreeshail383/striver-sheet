class Solution:
    def oddDigit(self, n):
        oddCount = 0
        while n > 0:
            lastdigit = n % 10
            if lastdigit % 2 == 1:
                oddCount += 1
            n = n // 10
        return oddCount

s = Solution()
print(s.oddDigit(7789))