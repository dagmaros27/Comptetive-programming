class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        setter = set()
        for r in range(len(s)):
            while s[r] in setter:
                setter.remove(s[l])
                l+=1
            setter.add(s[r])
            longest = max(longest,r-l +1)
        return longest
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        setter = set()
        for r in range(len(s)):
            while s[r] in setter:
                setter.remove(s[l])
                l+=1
            setter.add(s[r])
            longest = max(longest,r-l +1)
        return longest