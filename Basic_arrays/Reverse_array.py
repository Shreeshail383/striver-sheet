class Solution:
    def reverse(self, arr, l, r):
        if l >= r:
            return

        arr[l], arr[r] = arr[r], arr[l]

        self.reverse(arr, l + 1, r - 1)


s = Solution()
arr = [2, 4, 1, 3, 2]

s.reverse(arr, 0, len(arr) - 1)

print(arr)