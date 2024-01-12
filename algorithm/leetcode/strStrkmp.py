class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        # 暴力求解
        l1 = len(haystack)
        l2 = len(needle)
        if l1 < l2:
            return False
        p = 0
        q = 0
        while p<l1:
            tem = p
            while q<l2:
                if haystack[p] == needle[q]:
                    p += 1
                    q += 1
                else:
                    q = 0
                    p = tem + 1
                    break
            if q == l2:
                return p - l2
        return -1


if __name__ == '__main__':
    s1 = "sadbutsad"
    s2 = "sad"
    s = Solution().strStr(s1, s2)
    print(s)