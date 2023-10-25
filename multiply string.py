class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        hashmap = {}
        for i in range(10):
            hashmap[str(i)] = i

        a = 0
        deci_pos = 1
        for i in range(len(num1)-1, -1, -1):
            a += hashmap[num1[i]] * deci_pos
            deci_pos *= 10

        b = 0
        deci_pos = 1
        for i in range(len(num2)-1, -1, -1):
            b += hashmap[num2[i]] * deci_pos
            deci_pos *= 10

        return str(a * b)