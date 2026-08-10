class Solution:
    def addDigits(self, num: int) -> int:
        digit=0
        while num>=10:
            add=0
            while num>0:
                digit = num%10
                num//=10
                add+= digit
            num=add   
        return num