class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in word:
            i = word.find(ch)
        return word[:i + 1][::-1] + word[i + 1:]
    