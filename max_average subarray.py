class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total =  sum(nums[0:k])
        max_avg = total/k      
        for i in range(k, len(nums)):
            total = (total + nums[i]) - nums[i-k]
            avg = (total)/k
            max_avg = max(max_avg, avg)
        return max_avg