class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
        ans =  sorted(d.items(),key = lambda t: t[1], reverse = True)
        output = [ans[i][0] for i in range(k)]
        return output