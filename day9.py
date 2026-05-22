
'''
#NESTED LOOP-->LOOP INSIDE THE LOOP
for i in range(1,10):
    for j in range(1,2):
        print(i)
        print(j)

num=9
for j in range(1,11):
print(num*3)

#TO PRINT TABLE
num=9
for j in range(1,11):
    print(f"{num}*{j}={j*num}")

PALINDROME

so=input("enter a word:")
empty_str=""
for j in so:
    empty_str=j+empty_str
    print(empty_str)
if empty_str==so:
    print(f"{so} ia palindrome")
else:
    print(f"{so} is not  a palindrome")

#ARMSTRONG NUMBER

num=int(input("enter a number:"))
amstro_=0
length_=len(str(num))
for i in str(num):
    amstro_+=int(i)**length_
if amstro_==num:
    print(f"{num} is a amstro number")
else:
    print(f"{num} is not amstro number")
    

#PERFECT NUMBER
num=int(input("enter a number:"))
per_nu=0
for j in range(1,num):
    if num%j==0:
        per_nu+=j
        if per_nu==num:
            print(f"{num} is a perfect number num")
else:
     print(f"{num} is not a perfect number")
     

#PRIME NUMBER
num=int(input("enter a number:"))
count=0
for k in range(1,num+1):
    if num%k==0:
        count+=1
if count==2:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
'''

star=5
for d in range(1,star+1):
    for v in range(1,d+1):
        print("*",end="")
    print()


star=5
for d in range(1,star+1):
    for v in range(1,d+1):
        print(chr(64+v),end=" ")
    print()

A 
A B 
A B C 
A B C D 
A B C D E 


star=5
count=0
for d in range(1,star+1):
    for v in range(1,d+1):
        count+=1
        print(v,end=" ")
    print()
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5     


star=5
count=0
for d in range(star,0,-1):
    for v in range(1,d+1):
        count+=1
        print(v,end=" ")
    print()
    

1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 



num=5
for j in range(1,num+1):
    print(" "*(num-j),end="")
    for i in range(1,j+1):
          print("*",end=" ")
    print()      

  * 
   * * 
  * * * 
 * * * * 
* * * * * 
    

















     













          
    
