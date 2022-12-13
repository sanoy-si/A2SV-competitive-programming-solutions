#!/bin/python3

import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    for i in range(1,n):
        j=i-1
        k=arr[i]
        while j>=0 and k<arr[j]:
            arr[j+1]=arr[j]
            j-=1
            print(*arr)
        arr[j+1]=k
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
