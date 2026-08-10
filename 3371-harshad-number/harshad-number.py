class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum_digits = 0
        temp = x
        while temp > 0:
            digit = temp % 10
            sum_digits += digit
            temp = temp//10
        if x % sum_digits!= 0:
            return -1
        else:
            return sum_digits