import math
import time

def diag_sum():
    diff = 2
    x = 1
    num_list = []
    while True:
        for i in range(4):
            x += diff
            num_list.append(x)
        diff += 2
        if 1002001 in num_list:
            break
    return sum(num_list) + 1 

print(diag_sum())


    