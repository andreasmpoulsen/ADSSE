import numpy as np
import math

A = (np.sqrt(5)-1)/2

def calc(k):
    return math.floor(1000*(k*A%1))

print(calc(65))