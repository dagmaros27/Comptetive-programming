class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
            #brute force
            # start = 0
            # for end in range(len(nums)):
            #     if nums[end] == 0:
            #         k -= 1
            #     if k < 0:
            #         if nums[start] == 0:
            #             k += 1
            #         start += 1
            # return end - start + 1


            hmap = defaultdict(int)
            length = 0
            l =0
            for r in range(len(nums)):
                hmap[nums[r]] += 1

                while hmap[0] > k:
                    hmap[nums[l]] -= 1
                    l += 1
                length = max(length, hmap[0] + hmap[1])

            return length 
