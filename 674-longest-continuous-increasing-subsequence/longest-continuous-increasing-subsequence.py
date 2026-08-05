class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count = 1
        max_count = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
            else:
                if max_count < count:
                    max_count = count
                count = 1
        return max(count, max_count)