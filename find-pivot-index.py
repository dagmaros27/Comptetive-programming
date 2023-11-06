class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        #brute force
        # for i in range(len(nums)):
        #     sum1,sum2=0,0
        #     j = 0
        #     while j < len(nums):
        #         if j<i:
        #             sum1 += nums[j]
        #         if j>i:
        #             sum2 += nums[j]
        #         j += 1
        #     if sum1 == sum2:
        #         return i
        # return -1


        prefix = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        for i in range(len(prefix) - 1):
            if prefix[i] == prefix[len(nums)] - prefix[i + 1]:
                return i
        return -1