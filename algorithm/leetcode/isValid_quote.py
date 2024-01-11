class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        right = [')', '}', ']']
        mapping = {')': '(', '}': '{', ']': '['}
        for sub_s in s:
            # 如果当前括号是右类括号，进入下面if语句
            if sub_s in right:
                '''
                当栈为空, 遇见右类括号直接返回False
                若栈不为空, 检查当前括号和栈尾括号是否匹配
                    1. 若匹配，则将栈尾括号出栈，然后继续遍历
                    2. 若不匹配，即发现了异常括号对，则返回False
                '''
                if not stack:
                    return False
                if mapping[sub_s] == stack[-1]:
                    stack.pop()
                    continue
                else:
                    return False
            # 非右类括号不做判断直接入栈
            stack.append(sub_s)
        # 如果栈为空代表所有括号都相互抵消, 即不存在异常括号对，则返回True. 反之返回False
        return len(stack) == 0

if __name__ == '__main__':
    s = '()[]{}'
    Solution().isValid(s)