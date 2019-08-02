#!/bin/python

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    

    for i in range(1,n+1):

        for j in range(0,n-i):
           sys.stdout.write(' ')
        for k in range(1,i+1):
            sys.stdout.write('#')
        sys.stdout.write('\n')
           
if __name__ == '__main__':
    n = int(raw_input())

    staircase(n)
