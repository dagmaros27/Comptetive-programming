class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        #brute force
        # subarr = 0
        # for i in range(len(nums)):
        #     odd_counter = 0
        #     j = i
        #     while j < len(nums):
        #         if nums[j] %2 != 0:
        #             odd_counter += 1
        #             if odd_counter == k:
        #                 subarr += 1
        #         if nums[j] %2 == 0 and odd_counter ==k:
        #             subarr+=1
        #         j += 1
        # return subarr

        odd = 0
        l = 0
        subarr = 0
        count = 0 #this counts the subarrs when the left pointer moves
        for r in range(len(nums)):
            if nums[r] %2 == 1:
                odd += 1
                count = 0
            while odd == k:
                if nums[l] %2 == 1:
                    odd -= 1
                l += 1
                count += 1
            subarr += count
        return subarr
            