# 某套连招动作记作仅由小写字母组成的序列 arr，其中 arr[i] 第 i 个招式的名字。请返回第一个只出现一次的招式名称，如不存在请返回空格。
# 示例 1：
#
# 输入：arr = "abbccdeff"
# 输出：'a'
# 示例 2：
#
# 输入：arr = "ccdd"
# 输出：' '
class Solution:
    def dismantlingAction(self, arr: str) -> str:
        lt = len(arr)
        for i in range(lt):
            tem = arr.count(arr[i])
            if tem == 1:
                return arr[i]
        else:
            return " "

    # 标准--哈希表法
    def firstUniqChar(self, s: str) -> str:
        dicts = {}
        for i in s:
            dicts[i] = dicts.get(i, 0) + 1
        for i in s:
            if dicts[i] == 1:
                return i
        return ' '


if __name__ == '__main__':
    s = 'abbccdeff'
    m = Solution().dismantlingAction(s)
    print(m)