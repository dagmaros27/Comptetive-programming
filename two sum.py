class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sett = {}
        for ind, num in enumerate(nums):
            otherNum = target-num
            if otherNum in sett and ind != sett[otherNum]:
                #the and part is extra since set is unique
                   return [sett[otherNum], ind]
            sett[num] = ind         
        return