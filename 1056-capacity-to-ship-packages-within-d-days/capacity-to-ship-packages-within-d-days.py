def canShip(weights, days_have, capacity):
    sm = 0
    days_needed = 1
    for weight in weights:
        if sm + weight <= capacity:
            sm += weight
        else:
            days_needed += 1
            sm = weight        
    return days_needed <= days_have

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)    
        while low < high:
            mid = (low + high) // 2
            if canShip(weights, days, mid):
                high = mid
            else:
                low = mid + 1
        return low