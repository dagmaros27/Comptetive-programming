class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        set = {'a','e','i','o','u'}
        l = 0
        max_vowel = 0
        curr_vowel = 0

        for r in range(len(s)):
            if s[r] in set:
                curr_vowel += 1
            max_vowel = max(max_vowel, curr_vowel)
            if r-l+1 == k:
                if s[l] in set:
                    curr_vowel -= 1
                l += 1
        return max_vowel
        