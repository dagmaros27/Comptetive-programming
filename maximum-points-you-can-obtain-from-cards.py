class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        n = len(cardPoints)
        

        subarr_sum = sum(cardPoints[0:n-k])
        minSum = subarr_sum
        for r in range(n-k,n):
            curSum = subarr_sum - cardPoints[r-(n-k)] + cardPoints[r]
            minSum = min(minSum,curSum)
        return total - minSum

#the classic left right pointer doesn't work here because the examples 
and the description is misleading so use the subarray
