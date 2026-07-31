class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_ = 0
        product = 1
        digit =0
        while n>0:
            digit = n%10
            product *= digit
            sum_ += digit
            n=n//10
        return product - sum_