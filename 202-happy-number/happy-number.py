class Solution:
    def isHappy(self, n: int) -> bool:    
        while n >= 10:
            sm = 0
            while n > 0:
                digit = n % 10
                sm += digit**2
                n//= 10
            n = sm
        return n == 1 or n == 7