class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
            #brute force
            #hard to find the brute force


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
