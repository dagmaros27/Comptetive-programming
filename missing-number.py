class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxNum = max(nums)
        sum = int((maxNum * (maxNum+1))/2)
        for i in range(len(nums)):
            sum -= nums[i]
        if sum not in nums:
            return sum
        else:
            return maxNum +1