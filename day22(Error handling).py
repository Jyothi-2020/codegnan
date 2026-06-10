#Error Handling
'''

try block
---------
->The try block,test a block of code for error

except lock
------------
->The except block let hand if the code contain errors

else block
----------
->This will be excuted,if the try block has no error in the code

finally block
-------------
->This will be excuted either try block contain error or not


try:
    print(10/0)
except:
    print("This will handle zerodivision error")

try:
    print(a)
except:
    print("jyothi")
    
try:
    print(9)
except:
    print(9+10)

try:
    print(len(a))
except:
    print("jbdbuisfiegfqbjqhfug")


try:
    print(10/0)
except:
    print("This will handle zerodivision error")
else:
    print("no error")

try:
    a=10
    print(a+b)
except NameError:
    print("Name Error")
else:
    print("No Error")
    
op:Name Error->A NameError occurs when you use a variable that has not been defined.

    
    
try:
    a = 10+"5"
except TypeError:
    print("Type Error")
else:
    print(a)
    
op:Type Error->A TypeError occurs when an operation is performed on incompatible data types.


try:
    print("hai")
except:
    print("error")
else:
    print("no error")
finally:
    print("end")
op:hai
   no error
   end 
   

try:
    a=10
    print(b)
except:
    print("error")
else:
    print("no error")
finally:
    print("end")
    
op:error
   end
'''    

try:
    d={1:"Apple",2:"Banana"}
    print(d[3])
except:
    print("error")
else:
    print("no error")
finally:
    print("end")
       
















    




    
