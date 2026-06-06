
'''
#polymorphism
->this means 'many forms'. it allows the same function,method or operator to behave differently depending on the object.
1.Method overloading
---------------------
->Method overloading means defining multiple methods with the same name but different paramaters.

eg 1
class calculator:
    def add(self,a,b):
        return a+b
an=calculator()
print(an.add(30,23))
print(an.add(30,23,9))

eg 2
class calculator:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c=0):
        return a+b+c
an=calculator()
print(an.add(30,23))
print(an.add(30,23,9))


2.Method overriding
--------------------
->This occurs when a child class provides its own implementation of a method already defined in the parent class.

class animal:
    def sound (self):
        print("Animal makes sound")
class Dog(animal):
    def sound(self):
        print("Dog barks")

ntg=Dog()
ntg.sound()

3.Operator overloading
-----------------------
->This allows operators such as +,-,*etc, to perform different actions for user-defined objects.
note:the other operator inside the method will overload a special 
eg 1

class stu:
    def __init__(self,marks):
        self.marks=marks
    def __add__(self,other):
        return self.marks+other.marks
so=stu(60)
any=stu(56)
print(so+any)

eg 2
class stu:
    def __init__(self,marks):
        self.marks=marks
    def __add__(self,other):
        return self.marks*other.marks
so=stu(60)
any=stu(56)
print(so+any)





Abstraction
------------
->This is the process of hiding internal implementation details and showing only essential features to the user.
->It focuses on what an object does rather than how t does it.'''


from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeters(self):
        pass
class Rec(shape):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def area(self):
        return self.a*self.b
    def parameters(self):
        return 2*(self.a*self.b)
an=Rec(10,5)
print(an.area())











