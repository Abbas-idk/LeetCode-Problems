class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = 0
        new=[]
        for i in nums:
            running_sum += i
            new.append(running_sum)
        return new