#import leetcode


class ClassMath:
    numOfObjects = 0
    def __init__(self, val):
        self.val = val
        ClassMath.numOfObjects += 1

    def sayVal(self):
        print(f'Hi! i am an object and my value is {self.val}')


    def func1():
        print('Trigger func1')


    @staticmethod
    def howMany():
        print(ClassMath.numOfObjects)


ClassMath(8)
ClassMath(2)
ClassMath(3)
print(ClassMath.numOfObjects)

print(ClassMath.howMany())


print(ClassMath.numOfObjects)


def func2():
    print('Trigger func2')


# COMMENTS SHOW OUTPUT


#----------------------------------------------------------------------------------
#   Calling functions
#----------------------------------------------------------------------------------
#                               Syntax: File.Class.Function()

func2() # Trigger func2

ClassMath.func1() # Trigger func1

#leetcode.Solution.func3() # Trigger func3

ClassMath.howMany() # 0

#----------------------------------------------------------------------------------
#   Creating Objects
#----------------------------------------------------------------------------------
#                           Syntax: Class({paramaters from __init__})

ClassMath(8)
ClassMath.howMany() # 1
ClassMath(3)
ClassMath(5)
ClassMath(1)
ClassMath.howMany() # 4

#----------------------------------------------------------------------------------
#   Using a Objects method (function)
#----------------------------------------------------------------------------------
#                       Syntax: Object.Function      Or     Object.Attribute

Jeff = ClassMath(4000)


print(Jeff.val) # 4000

Jeff.sayVal()   # Hi! i am an object and my value is 4000










class A:
    def __init__(self, wage):
        self.wage = wage
        
        self.id = 7

class B:
    def __init__(self, wage):
        self.wage = wage
        
        self.id = 8

        wage


jeff = A(4000)
bob = A(4000)
sally = A(4000)



print(jeff.id)
print(bob.id)
print(sally.id)





ted = B(3000)

def saywage(cls):
    print(cls.wage)



def give(cls, wage):
    wallet += cls.wage
