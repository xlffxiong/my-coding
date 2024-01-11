# 教练使用整数数组
# actions
# 记录一系列核心肌群训练项目编号。为增强训练趣味性，需要将所有奇数编号训练项目调整至偶数编号训练项目之前。请将调整后的训练项目编号以
# 数组
# 形式返回。
#
#
#
# 示例
# 1：
#
# 输入：actions = [1, 2, 3, 4, 5]
# 输出：[1, 3, 5, 2, 4]
# 解释：为正确答案之一
class Solution:
    def trainingPlan(self, actions):
        m = len(actions)
        n = 0
        for i in actions:
            if i % 2 == 0:
                n = n + 1
        print(n)
        for k in range(n+2):
            print(f"{k}轮开始")
            for i in range(m-2, -1, -1):
                print(f' i is {i}, actions[i] is {actions[i]}')
                if actions[i] % 2 == 0 and actions[i + 1] % 2 != 0:
                    actions[i], actions[i + 1] = actions[i + 1], actions[i]
                    print(actions)
            print(f"第{k}次 {actions}")
        # 左边遍历拿到偶数
        l_k, l_v = 0, 0
        for _i, _v in enumerate(actions):
            if _v % 2 == 0:
                l_k = _i
                l_v = _v
                break
        r_k, r_v = 0, 0
        for _j, _jv in enumerate(actions[::-1]):
            if _jv % 2 != 0:
                r_k = _j
                r_v = _jv
                break
        print(l_k, l_v, len(actions) - r_k, r_v)
        if l_k < len(actions) - r_k:
            actions[l_k], actions[len(actions) - r_k] = actions[len(actions) - r_k], actions[l_k]
        return actions

    def trainingPlan1(self, actions):
        m = len(actions)
        i = 0
        j = m-1
        while i < j:
            if actions[i] % 2 != 0 and i < j:
                i = i + 1
            if actions[j] % 2 == 0 and i < j:
                j = j - 1
            actions[i], actions[j] = actions[j], actions[i]
        return actions


if __name__ == '__main__':
    s=[2,16,3,5,13,1,16,1,12,18,11,8,11,11,5,1]
    m=Solution().trainingPlan1(s)
    print(m)
