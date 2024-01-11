class Solution:
    def climbStairs1(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1 or n == 2:
            return n
        return self.climbStairs1(n-1) + self.climbStairs1(n-2)
    def climbStairs2(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b


if __name__ == '__main__':
    print(Solution().climbStairs1(4))