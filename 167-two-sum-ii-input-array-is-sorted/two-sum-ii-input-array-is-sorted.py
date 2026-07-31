class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sum =0
        left = 0
        right = len(numbers) - 1
        while left < right:
            for i in range(0,len(numbers)-1):
                sum = numbers[left] + numbers[right]
                if sum > target:
                    right-=1
                elif sum < target:
                    left+=1
                else:
                    return left+1, right+1