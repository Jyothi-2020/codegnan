'''
#FIBONACCI SERIES
#---------------
num=0
num2=1
def finaaci(num,num2):
    limit_=int(input("enter the limit:"))
    print(num,num2,end=" ")
    for i in range(1+limit_):
        num3=num+num2
        num=num2
        num2=num3
        print(num3,end=" ")
finaaci(num,num2)
op:enter the limit:10
   0 1 1 2 3 5 8 13 21 34 55 89 144
   

#remove duplicates
   
any=[2,5,7,9,2,7]
new_=[]
def Dup(any,new_):
    for j in any:
        if j not in new_:
            new_.append(j)
    print(new_)
Dup(any,new_)
'''

#split
count=0
so="Quantum computing uses the principles of quantum mechanics to process complex information exponentially faster than classical computers".split()
def word_str(so,count):
    for j in so:
        count +=1
    print(count)    
word_str(so,count)

    



