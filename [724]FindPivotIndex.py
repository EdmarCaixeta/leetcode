from typing import List


def pivotIndex(nums: List[int]) -> int:
    listSum = sum(nums)
    aux = listSum
    for index, item in enumerate(nums):
        aux -= item

        if(index == len(nums) -1):
            break

        if(abs(aux) < (listSum/2)):
            return nums.index(item)
    return -1

print(pivotIndex([-1,-1,-1,-1,-1,-1]))

'''
[1,7,3,6,5,6]
    sum: 28
    28 - 1 = 27
    27 - 7 = 20
    20 - 3 = 17
    17 - 6 = X = 11 < (28 / 2)
    salva pivot e verifica soma da frente
    5 + 6 = 11 == X retorna indice

[2,1,-1]
    sum: 2
    2-2 = X = 0 < 2/2 
    salva pivot e verifica a soma da frente
    1 + (-1) = 0 == X, retorna indice

[1,2,3]
    sum: 6
    6 - 1 = 5
    5 - 2 = 3
    3 - 3 = 0 < 6 / 2
    acabou todos os valores da [] então retorna -1
'''