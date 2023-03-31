import math
import os
import random
import re
import sys
def countSwaps(a):
    count=0
    for num1 in range(n):
        for num2 in range(n-1):
            if a[num2]>a[num2+1]:
                a[num2],a[num2+1]=a[num2+1],a[num2]
                count+=1
    print("Array is sorted in",count,"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1])
        
    
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
