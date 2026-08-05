class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Sliding Window (Fixed-length Sliding Window)
        maxAverage = -10000000
        left = 0
        currentSum = 0
        for right in range(len(nums)):
            currentSum += nums[right]
            if right >= k - 1:
                avg = currentSum / k
                maxAverage = max(avg, maxAverage)
                # Subtracting the value on left (Window Size is exceed k)
                currentSum -= nums[left]
                left += 1
        return maxAverage