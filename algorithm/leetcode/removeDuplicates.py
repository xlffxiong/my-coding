# 给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。
class Solution:
    def removeDuplicates(self, nums):
        # 方一：基于数据结构处理
        # 集合set() 比对--集合会改变添加进入的顺序
        # --> 用列表`append()+单个元素`
        col = []
        for i in range(len(nums)):
            if nums[i] not in col:
                col.append(nums[i])

        k = len(col)
        nums[:k] = col
        return k


if __name__ == '__main__':
    n = [1,1,2]
    m = Solution().removeDuplicates(n)
    print(m)
