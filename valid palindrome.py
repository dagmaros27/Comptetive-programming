class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []

        for i in range(len(s)):
            if s[i].isalnum():
                arr.append(s[i])
        word = "".join(arr).lower()
        front, back = 0, len(word)-1
        while front < back:
            if word[front] != word[back]:
                return False
            front+=1
            back-=1
        return True
