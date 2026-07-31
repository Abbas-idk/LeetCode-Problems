def is_v(ch):
    return ch in "aeiouAEIOU"
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left =0
        right = len(s) - 1
        while left < right:
            if is_v(s[left]) and is_v(s[right]):
                s[left] , s[right] = s[right] , s[left]
                left += 1
                right -= 1
            elif is_v(s[left]):
                right-=1
            elif is_v(s[right]):
                left+=1
            else:
                left+=1
                right-=1
        return ''.join(s) 