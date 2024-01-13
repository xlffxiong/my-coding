# 179 最大数
# 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
#
# 注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
# 思路
# 两个数字对应的字符串a和b，如果字典序a+b>b+a，此时a排在b的前面即可获得更大值
# 示例：a=3,b=32,两者拼接的值：332>323，所以3应排在32前面
# 复杂度分析
# 时间复杂度：O(n2n^2n
# 2
#  )
# 空间复杂度：O(nnn)
#
# 作者：追风少年
# 链接：https://leetcode.cn/problems/largest-number/solutions/717342/python3-san-chong-fang-fa-qiu-zui-da-shu-cpi4/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def largestNumber(self, nums):
        n = len(nums)
        nums = list(map(str, nums))
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        # ['9', '5', '34', '3', '30']
        # 这样最大
        return str("".join(nums))


if __name__ == '__main__':
    n = [3,30,34,5,9]
    m = Solution().largestNumber(n)