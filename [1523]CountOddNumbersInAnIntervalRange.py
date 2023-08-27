def countOdds(low: int, high: int) -> int:
    intervalSize = high - (low - 1)
    lowParity = low % 2 == 0
    highParity = high % 2 == 0

    if lowParity != highParity:
        return int(intervalSize / 2)
    
    if lowParity == highParity:
        if lowParity == False:
            return int(intervalSize / 2) + 1
        else:
            return int(intervalSize / 2)

print(countOdds(3,7))

'''
[1,2,3,4,5,6,7,8,9,10]:
    initial: 1 (odd)
    final: 10 (even)
    size: 10
    odds: 5
    even: 5

[3,4,5,6,7]:
    initial: 3 (odd)
    final: 7 (odd)
    size: 5
    odds: 3
    even: 2

[2,3,4,5,6,7,8]:
    initial: 2 (even)
    final: 8 (even)
    size: 7
    odds: 3
    even: 4

Odd + Odd = Even
5 + 7 = 12
9 + 5 = 16

Odd + Even = Odd
5 + 2 = 7
7 + 8 = 15

Even + Even = Even
10 + 10 = 20
2 + 8 = 10
'''