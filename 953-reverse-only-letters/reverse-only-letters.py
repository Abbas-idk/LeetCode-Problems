class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            if not ans[i].isalpha():
                i += 1
            elif not ans[j].isalpha():
                j -= 1
            else:
                ans[i], ans[j] = ans[j], ans[i]
                i += 1
                j -= 1
        return "".join(ans)