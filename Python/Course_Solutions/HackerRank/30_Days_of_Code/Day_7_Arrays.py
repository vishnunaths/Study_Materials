Day 7: Arrays	
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    arr = arr[::-1]
    arr = ' '.join(str(e) for e in arr)
    print(arr)