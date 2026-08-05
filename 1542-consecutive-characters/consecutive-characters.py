class Solution:
    def maxPower(self, s: str) -> int:
        count = 1
        max_count = 1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                count += 1
            elif s[i]!= s[i-1]:
                if count > max_count:
                    max_count=count
                count = 1
        return max(count, max_count)