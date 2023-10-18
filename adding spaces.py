class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        sentence = ""
        index = 0
        for i in spaces:
            sentence += s[index:i]
            sentence += " "
            index = i
        sentence += s[index:]
        return sentence