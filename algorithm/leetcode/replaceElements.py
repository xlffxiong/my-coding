class Solution:
    def replaceElements1(self, arr):
        res = []
        if (len(arr)) == 1:
            return [-1]
        for i in range(1, len(arr)):
            res.append(max(arr[i:]))
        res.append(-1)
        return res

    def replaceElements2(self, arr):
        for index, el in enumerate(arr):
            arr[index] = max(arr[index + 1:]) if (index != len(arr) - 1) else -1
        return arr

    # 倒序求解
    def replaceElements3(self, arr):
        n = len(arr)
        res = [0] * (n - 1) + [-1]
        for i in range(n - 2, -1, -1):
            res[i] = max(arr[i + 1], res[i + 1])
        return res

# pass
if __name__ == '__main__':
    a = [17, 18, 5, 4, 6, 1]
    m = Solution().replaceElements1(a)
    print(m)