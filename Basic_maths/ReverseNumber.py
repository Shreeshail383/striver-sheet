def reverseNumber(n):
    rev = 0
    while n > 0:
        lastdigit = n % 10
        n = n // 10
        rev = rev * 10 + lastdigit
    return rev

n = 1234
print(reverseNumber(n))


#leetcode 7. Reverse Integer
class Solution:
    def reverseNumber(self, x):
        res = 0
        if x < 0:
            res = int(str(x)[1:][::-1] ) * -1
        else:
            res = int(str(x)[::-1])
        return res
s = Solution()
print(s.reverseNumber(-1234))