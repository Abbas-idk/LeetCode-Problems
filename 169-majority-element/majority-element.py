class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        count = 0
        for num in nums:
            if count == 0:
                d = num
            if num == d:
                count += 1
            else:
                count -= 1
        return d