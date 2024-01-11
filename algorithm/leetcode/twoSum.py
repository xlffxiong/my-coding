class Solution:
    def twoSum(self, nums, target):
        lt = len(nums)
        print(lt)
        for i in range(lt-1, 0, -1):
            print(i)
            if target - nums[i] in nums:
                t = nums.index(target - nums[i])
                if t == i:
                    continue
                else:
                    res = [t, i]
                    break
        return res


if __name__ == '__main__':
    n = [2,4,11,3]
    m = Solution().twoSum(n, 6)
    print(m)