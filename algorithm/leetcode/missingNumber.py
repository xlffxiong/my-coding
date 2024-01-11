# 给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数
class Solution:
    def missingNumber(self, nums) -> int:
        n = len(nums)
        target_int = [i for i in range(n+1)]
        print(target_int)
        for i in target_int:
            if i not in nums:
                return i
    # 最优解决方法
    def missingNumber02(self, nums):
        m = sorted(nums)
        print(m)
        for i in range(len(m)):
            if i != m[i]:
                return i


if __name__ == '__main__':
    l = [3, 0, 1]
    s = Solution().missingNumber02(l)
    print(s)