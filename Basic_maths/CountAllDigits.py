class Solution:
    def countdigit(self, n):
        count = 1 if n == 0 else 0
        while n > 0:
            count += 1
            n = n // 10
        return count

s = Solution()
print(s.countdigit(1234))