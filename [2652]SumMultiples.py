class Solution:
    def sumOfMultiples(self, n: int) -> int:
        sumation = 0
        for i in range(n+1):
            if i % 3 == 0:
                sumation += i
            elif i % 5 == 0:
                sumation += i
            elif i % 7 == 0:
                sumation += i
            else:
                continue
        return sumation
