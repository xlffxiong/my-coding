import string
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # 26进制的算法
        lt = len(columnTitle)
        hash_map = {}
        all_capital_letters = string.ascii_uppercase
        for i in all_capital_letters:
            hash_map[i] = ord(i)-64
        print(hash_map)
        if lt == 1:
            return hash_map[columnTitle]
        # for j in range(lt-1, -1, -1):
        #     print(columnTitle[j])
        res = 0
        for j in range(lt):
            res += hash_map[columnTitle[j]]*26**(lt-1-j)
            print(j, res)
        return res

if __name__ == '__main__':
    Solution().titleToNumber("ZY")