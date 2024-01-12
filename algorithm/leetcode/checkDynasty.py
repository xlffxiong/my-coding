# LCR 186 文物朝代判断
# 剑指 offer 61
# 展览馆展出来自 13 个朝代的文物，每排展柜展出 5 个文物。某排文物的摆放情况记录于数组 places，其中 places[i] 表示处于第 i 位文物的所属朝代编号。
# 其中，编号为 0 的朝代表示未知朝代。请判断并返回这排文物的所属朝代编号是否连续（如遇未知朝代可算作连续情况）

# 一句话描述，就是0代表万能排，看是否是顺子

# 示例 1：
#
# 输入: places = [0, 6, 9, 0, 7]
# 输出: True
#
#
# 示例 2：
#
# 输入: places = [7, 8, 9, 10, 11]
# 输出: True

class Solution:
    def checkDynasty(self, places):
        lt = len(places)
        places.sort()
        num_0 = places.count(0)
        if num_0 == lt:
            return True
        max_num = places[-1]
        while lt:
            if max_num in places:
                max_num -= 1
            else:
                num_0 -= 1
                print(f"使用万能排一张,剩余数目 {num_0}")
                max_num -= 1
                if num_0 < 0:
                    return False
            lt -= 1
        print(lt, num_0)
        return True


if __name__ == '__main__':
    places = [0,0,2,2,5]
    m = Solution().checkDynasty(places)
    print(m)