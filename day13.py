
'''
LIST COMPREHENSION
------------------
-->this list comprehension offers a shortest syntax when we want to create a new list from exisying list
syntax-->vari_name=[expression loop condition]
old=[1,2,3,4,5]
new=[so for so in old]
print(new)
op:[1, 2, 3, 4, 5]

old=[1,2,3,4,5]
new=[so for so in old if so%2==0]
print(new)
op:[2, 4]

#to print even in even number places
old=[1,2,3,4,5,6]
new=[so if so%2!=0 else "even" for so in old]
print(new)
op:[1, 'even', 3, 'even', 5, 'even']

#GENERATORS
---------------
-->generators in python are a special type of itterable,allowing users to iterate over data efficiently without storing everyting in memeory...
-->they generae values lazily using yield keyword

def simple_gen():
    print("start")
    yield 1
    yield 2
    yield 3
    print("end")
gen=simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))
op:start
1
2
3

WHY TO USE GEN
--------------
Generators do not store the entire dataset in memory,they generate values on the fly a run time.
Avoiding unnecessary storage of data speed up execution.

HOW IT WORKS
--------------
it looks like normal function but uses the yield keyword instead of return
wen the function is called, it does not execute immediately.instead,it return a generator object which can be iterated using loop or the next() function

def any(num):
    for i in range(num):
        yield i*i
a=any(5)
print(next(a))

op:0

def any(num):
    for i in range(num):
        yield i*i
a=any(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
op:
0
0
1
4
9

def sqr(num):
    result=[]
    for i in range (1,num+1):
        result.append(i*i)
    return result
print(sqr(5))

op:[1, 4, 9, 16, 25]
'''

so='Quantum computing leverages the principles of quantum mechanics to process complex information exponentially faster than classical computers'
any=' '
for j in so:
    if j not in "AEIOUaeiou":
        any+=j
print(any)        

op: Qntm cmptng lvrgs th prncpls f qntm mchncs t prcss cmplx nfrmtn xpnntlly fstr thn clsscl cmptrs







































