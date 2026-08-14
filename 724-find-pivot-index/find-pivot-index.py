class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = [0]
        n = len(nums)
        sum_nums = 0
        for i in nums:
            sum_nums += i
            prefix_sum.append(sum_nums)
        
        for i in range(len(nums)):
            left_sum = prefix_sum[i]
            right_sum = prefix_sum[n]-prefix_sum[i+1]
            if left_sum == right_sum:
                return i
        return -1