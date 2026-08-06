def is_v(ch):
    return ch in "aeiou"

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Compute the number of vowels in first
        # k-size substring
        first_window = s[:k]
        v_c = 0
        for i in first_window:
            if is_v(i):
                v_c += 1
        mx_v = max(0, v_c)
        for i in range(k, len(s)):
            if is_v(s[i]):   #New element
                v_c += 1
            if is_v(s[i-k]): # Leaving element
                v_c -= 1
            mx_v = max(mx_v, v_c)
        return mx_v