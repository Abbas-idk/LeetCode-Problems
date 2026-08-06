class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        left = 0
        currentSum = 0
        for right in range(len(arr)):
            currentSum += arr[right]
            if right >= k-1:
                avg = currentSum / k
                currentSum -= arr[left]
                left += 1
                if avg >= threshold:
                    count += 1
        return count