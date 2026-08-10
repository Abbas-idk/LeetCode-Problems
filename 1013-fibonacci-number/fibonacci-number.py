class Solution:
    def fib(self, n: int) -> int:
        if n <= 0:
            return n
        prev1 = 1
        prev2 = 0
        for i in range(1, n+1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return prev2