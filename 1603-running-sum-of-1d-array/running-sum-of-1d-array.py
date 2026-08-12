class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = 0
        new=[]
        for i in range(len(nums)):
            running_sum +=nums[i]
            new.append(running_sum)
        return new