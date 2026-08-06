class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        current_white = blocks[:k].count('W')
        min_white = current_white
        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                current_white += 1
            if blocks[i-k] == 'W':
                current_white -= 1
            min_white = min(min_white, current_white)
        return min_white