# 给你一个字符串 s，最多 可以从中删除一个字符。
#
# 请你判断 s 是否能成为回文字符串：如果能，返回 true ；否则，返回 false 。
# 1 <= s.length <= 105
# s 由小写英文字母组成

class Solution:
    def validPalindrome(self, s: str) -> bool:
        res = []
        if s == s[::-1]:
            return True
        else:
            for i in range(1, len(s)-1):
                tem_s = s[0:i] + s[(i+1):]
                print(i, tem_s)
                if len(tem_s) == len(s)-1:
                    res.append(self.validPalindrome(tem_s))
        print(res)
        if True in res:
            return True
        else:
            return False


if __name__ == '__main__':
    s = "abca"
    mm = Solution().validPalindrome(s)
    print(mm)
