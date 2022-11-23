import numpy as np
def reverse(x: int) -> int:
    MAX = 2147483647
    MIN = -2147483648
    x = np.int32(x)
    if(x >= MAX or x <= MIN):
        return 0
    
    x = str(x)
    result = str(x)[::-1]
    if(result[len(result)-1] == '-'):
        result = result.replace('-', '')
        result = '-' + result
    return int(result)
    

print(reverse(1534236469))