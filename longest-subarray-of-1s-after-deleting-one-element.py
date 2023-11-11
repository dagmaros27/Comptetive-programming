class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = 0
        current = 0
        l =0
        zeros = 0
        for r in range(len(nums)):
            current += 1
            if nums[r] == 0:
                zeros += 1
            while zeros > 1:
                if nums[l] == 0:
                    zeros -=1
                l += 1
            longest = max(longest, r-l)
        return longest

        #just compute the longest subarray of 1's with atmost one 0 and return length-1
        #this approach is just using sliding window dp solution can be more efficent
