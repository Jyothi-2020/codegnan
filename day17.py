
'''#INHERITANCE
->this allows one class  to acquire the properties and methods of another class.

#Types
1.single inheritance  parent--<child class
---------------------        
->A class inherits from a single parent class

class father:
    def Land(self):
        print("i am father have 5A")

class jyothi(father):
    def my_own(self):
        print('i have 2A')
fam=jyothi()
fam.Land()
    
op:i am father have 5A

2.Multiple inheritance    father,mother->child
-------------------------
-->A child class inherits from moe than one parent class
class father:
    def Land(self):
        print("i am father have 5A")
class mother:
    def gold(self):
        print("my mother have 1kg G")
        

class jyothi(father,mother):
    def mine(self):
        print('i have ntg')
all_=jyothi()
all_.Land()
all_.gold()

3.Multi-level inheritance   grandfather-->father-->child class
-------------------------
->A class inherits from a parent class and another class inherits from that child class.
class grandfather:
    def land(self):
        print("my grandfather have 5A of land")
class father(grandfather):
    def flat(self):
        print(" have flat at banglore")
        

class jyothi(father):
    def ntg(self):
        print('i own both of their p')
all_=jyothi()
all_.land()
all_.flat()
all_.ntg()

4.Hierarchical inheritance  parent-->child
--------------------------        -->child
->Multiple child classes inherits from a single parent.

class father:
    def land(self):
        print("10 A land")
class jyothi(father):
    def mine(self):
        print("job")
class bhavani(father):
    def sis(self):
        print("jobless")
bha=bhavani()
bha.land()

jyo=jyothi()
jyo.land()

5.Hybrid inheritance
--------------------
->This is the combination of two or more types of inheritance.

class A:
    def some(self):
        print('class A')
class B(A):
    def any(self):
        print('class B')
class C(A):
    def so(self):
        print('class C')
class D(B,C):
    def all(self):
        print('class D')
        
how=D()
how.so()
how.all()
how.any()
how.so()


#super method
--------------
->super() is used to access methods and constructor of the parent class from the child class'''

class parent:
    def display(self):
        print('Method parent')
class child(parent):
    def display(self):
        super().display()
        print('Method child')
any_=child()
any_.display()



class person:
    def __init__(self,name):
        self.name=name
class stu_(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll=roll
    def show(self):
        print(f"Name : {self.name}")
        print(f"Roll No :{self.roll}")
any_=stu_('jyothi',104)
any_.show()































        
        










