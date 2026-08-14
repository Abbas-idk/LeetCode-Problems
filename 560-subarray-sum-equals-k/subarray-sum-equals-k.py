class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Prefix + HashMap Solution
        cSum = 0 # This is our prefix sum
        subCnt = 0 # How many subarrays have we seen with sum k
        seen = {0: 1} # HashMap to store prefix sums found so far
        for i in nums:
            # Compute prefix sum
            cSum += i
            # Required prefix sum (prefix(l-1), history)
            req = cSum - k
            # Check if req in seen prefixes so far
            if req in seen:
                subCnt += seen[req] # add the number of times we seen that prefix
            # Push the current prefix in hashmap
            seen[cSum] = seen.get(cSum, 0) + 1
        return subCnt