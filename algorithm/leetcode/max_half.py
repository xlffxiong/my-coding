# 仓库管理员以数组 stock 形式记录商品库存表。stock[i] 表示商品 id，可能存在重复。请返回库存表中数量大于 stock.length / 2 的商品 id
# 输入: stock = [6, 1, 3, 1, 1, 1]
# 输出: 1
class Solution:
    def inventoryManagement(self, stock) -> int:
        # 数量/2
        n = len(stock)/2
        res_map = {}
        for i in stock:
            res_map[i] = 0
        for i in stock:
            if i in res_map:
                res_map[i] = res_map[i] + 1
        for k, v in res_map.items():
            if v > n:
                return k


if __name__ == '__main__':
    l = [6, 1, 3, 1, 1, 1]
    s = Solution().inventoryManagement(l)
    print(s)