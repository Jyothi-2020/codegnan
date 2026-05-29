'''
MODULES
--------
A modules in python is a file that cotains python code such as
->variables
->functions
->classes
->statements

TWO TYPE OF MODULES
---------------
->user-define
->built-in

import day14
print(day14.add(10,6))
print(day14.sub(30,20)) in day 13


def add(a,b):     (this program is (import)written in day 13)                     
    return a+b
def sub(a,b):
    return a-b

----------
import math
print(math.sqrt(25))
print(math.factorial(10))
print(math.pow(2,5))
-------------------
from math import sqrt
print(sqrt(25))
---------------------
import math as m
print (m.factorial(10))
print(m.pow(2,5))
--------------------
import os                 to create a file
os.mkdir("some pyhton")
--------------------
import os
os.remove("some python")
---------------------------
import sys
print(sys.version)
print(sys.exit)
print(sys.path)
----------------
import random
print(random.randint(1000,9999))
-------------------------------

'''
from collections import Counter,defaultdict
data=['a','b','c','d']
counter=Counter(data)
print(counter)

print(counter)
dd=defaultdict(int)
dd['missing']+=1
print(dd ['missing'])
print(dd)























