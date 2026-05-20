
'''
F-string


CONDITION STATEMENTS
--------------------
if-->to check the statement is true or not

num=6
if num%2==0:
    print(num,"is a even number")

if-else-->else in the if statement,incase the condition becomes false then it will enter into flow-back(else),it will execute whatever inside it

NUMBER IS EVEN OR ODD
---------------------
num=int(input("enter a number:"))
if num%2!=0:
    print(num,"is a odd number")
else:
    print(f"{num} is a even number")


ELIGIBLE TO VOTE
----------------
age_=int(input("enter a number:"))
if age_>=18:
    print("we are eligible to vote")
else:
    print(f"we have to wait for {18-age_}more years")



NUMBER
-------
num=8
num_2=15
if num >=num_2:
    print(f"{num} is greater number than{num_2}")
else:    
     print(f"{num_2} is greater number than{num}")


LEAP YEAR
----------
year_=2025
if(year_%4==0 and year_%100!=0) or year_%400==0:
    print(f"{year_} is a leap year")
else:
    print(f"{year_}is not a leap year")   
    

FIND A NUMBER IS POITIVE OR NEGATIVE
-------------------------------------
num=-9
if num>=0:
    print(f"{num} is a positive number")
else:
    print(f"{num} is a negative number")


TO CHECK PASS OR FAIL
-----------------------
marks_=int(input("enter your marks:"))
stu_name=input("enter your name: ")
if marks_>=45:
    print(f"{stu_name}your passed")
else:
    print(f"{stu_name}your failed")

    
num=75
if num%3==0 and num%5==0:
    print(f"{num} is divided by 3 and 5")
else:
    print(f"{num} not")
    
'''
signal_=input("enter \n1.red  \n2.green")

if signal_==1:
    print("pls stop")
else:
    print("go")
    


































     
