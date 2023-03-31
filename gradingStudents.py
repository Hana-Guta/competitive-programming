import math
import os
import random
import re
import sys

def gradingStudents(grades):
    for i in range(0,len(grades)):
        diff= 5-grades[i]%5
        mul= (grades[i]%5)
        if (grades[i]>37) and mul != 0 and diff < 3:
            grades[i]+= diff
    return (grades)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
