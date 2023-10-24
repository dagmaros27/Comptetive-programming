class Solution:
    def reverse(self, x: int) -> int:
        string = str(x)
        numstr = string[::-1]
        if numstr[-1] == '-':
            numstr = numstr[0:-1]
            num = -abs(int(numstr))
        else:
            num = int(numstr)
        if self.isValid(num):
            return num
        return 0
    def isValid(self,num)->bool:
        return  -2**31 <= num <= 2**31 - 1