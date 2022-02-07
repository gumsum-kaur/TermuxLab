"""import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")
"""
"""File Handling"
f = open("abc.txt", "a")
for i in (range(10)):
    f.write("Hello this is overwritten files\n");
f.close();

fp = open("abc.txt","r")

print(fp.read())   """

"""#if_else
if 5<2:
    print("five is greater than two")
else:
    print("false")"""
    
"""LongTextPrinting
txt =  This is a text file.
i can write anything anywhere here....inside the file.
You can can your of wrtitng anything anywhere here 
/.so let's see the result now.

print(txt)"""

"""#ValueOverwitten
x = 5;
x = "John";
x = 10;

print(x) """

"""#data types
x = str(3+4);
y = int(3+3);
z = float(3);

print(x,y,z);

print(type(x), type(y), type(z))"""

"""#Camel Case
myName = "Sailly";

#Pascal Case
MyName = "Milly"

#Snake Case
_my_name = "Gilly"

print(myName,"\n",MyName,"\n", _my_name);
"""

"""#Unpack/Unzip

fruits  = ["Apple","Banana", "Cherry"]

x,y,z =  fruits

print(x)
print(y)
print(z)"""

"""#ParameterizedFunctions
def myDetails(userName, userAge, userEmail) :
    name=userName;
    age = userAge;
    email=userEmail;
    print(name,"\n",age,"\n",email);
       
myDetails("Pankaj Kumar",25,"abcx@gmail.com");
myDetails("Rahul Kumar", 28, "rst@gmail.com");
myDetails("Sailly Kumari", 23, "sly@hotmail.com");
"""

""" FunctionsAll
def myFunc(*car) :
    print("New cars is "+ car[2]);
    
myFunc("Swift", "Tata", "Maruti", "Nano");
#-------------------------------------------------------------

def my_name(**child) :
    print("Child's last name is "+ child["lname"]);
    
my_name(fname="Rohan", lname="Chaurasiya");
#----------------------------------------------------------------------------

def myAbc(food) :
    for x in food:
        print(x)
        
fruits=["Apple", "Banana", "Cherry"]
 
myAbc(fruits)
#----------------------------------------------------------------------------

def myFunction(x) :
    return 5*x;
    
print(myFunction(4))
print(myFunction(5)) 
#-----------------------------------------------------------------------------

def myFunction() :
    pass;

#--------------------------------------------------------------------------"""

"""#Recursion in Function
def try_recursion(k):
    if(k>0):
        result = try_recursion(k-1)
        
        print(result)
        
    else:
       result=0
       return result
try_recursion(6)
"""

"""#Lambda

#x = lambda a : a + 10

#print(x(15))

#x = lambda a, b : a*b

#print(x(4,5))

def myfunc(n):
    return lambda a : a*n;
    
extra = myfunc(3)
extra1 = myfunc(2)

print(extra(10))
print(extra1(10))
"""

"""#Arrays

cars=["Volvo", "Toyota", "Swift"]

#for x in range(len(cars)):
cars.append("Honda")
cars.pop(0)
#cars.remove(3)

#for x in cars:
 #   print(x)
  
vehicle = cars.copy();
vehicle.insert(1,"Mahindra") 
#vehicle.reverse();
vehicle.sort()
for y in vehicle:
   print(y)
"""

"""#Count
points = [1,2,3,4,5,6,4,7,8,4]

x = points.count(4)

print(x)
"""

"""#Class&Objects
class myClass:
    x = 5
    #print(x)
    
obj = myClass()
print(obj.x);
"""

"""#Class&Objects_InDetails

class myClass:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
obj1 = myClass("Hanna", 29)
#del obj1.age 
print(obj1.name, obj1.age)

#-------------------------------------------

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def myFunc(self):
        print("\nHello, Name is ", self.name)

       
obj1 = Person("Hanna", 26)
obj1.myFunc()

#----------------------------------------------------"""

"""#Inheritance ImportantFacts

class myClassMate:                                        #Base Class or Parent Class
    def __init__(self, firstName, lastName):
        self.first_name = firstName
        self.last_name = lastName
        
    #def printValue(self):
        #print(self.first_name, self.last_name)
        
#obj = myClassMate("Kavya", "Mehra")
#obj.printValue()

class Student(myClassMate):                                                 # Derived Class or Child Class
 #   pass
    def __init__(self, firstName, lastName, year):                                 #Child have own init function
        #myClassMate.__init__(self, firstName, lastName)             #Parent Class's init fuction has been kept safe
        super().__init__(firstName, lastName)                         #Super function can also be used to inherit parent's property
        
        self.graduationYear = year
        
        
    def welCome(self):
        print("Welcome mr/ms ", self.first_name, self.last_name, " in ", self.graduationYear)
    
obj2 = Student("Angel", "Josef", 2023)
obj2.welCome()
"""

"""#Iterators (for example, list, tuples, dictionary, sets)

myTuple = ("Apple", "Banana", "Cherry", "Mango")

myIt = iter(myTuple)

print(next(myIt))
print(next(myIt))
print(next(myIt))
#--------------------------------

myStr = "Helllo"

myst = iter(myStr)
print(next(myst))
print(next(myst))

#----------------------------------

for x in myTuple:
    print(x);

#---------------------------------
for y in myStr:
    print(y)
"""

"""#Iteration in Class&Objects

class myNumbers:
    def __iter__(self):
        self.a = 1
        return self
        
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
        
obj = myNumbers()
myIter = iter(obj)

for x in myIter:
    print(x)
"""

"""#Scops  or global  & Function inside Function
def myFunction():
    x = 300
    
    def insideFunction():
        print(x)
        
    insideFunction()
    
myFunction()

#-------------------------

def  localVariable():
    y = 4000                    #local variable
    global z                    #global variable
    z = 5000
    
    print(y)
    
#print(y)                           # y is not accessible here because it is a local variable
localVariable()

print(z)"""

"""#Creating own Modules

#import myModule
import myModule as mx

a  = mx.person1["country"]
print(a)

#------------------------------------------------
from myModule import person2
 
x = person2["name"]
print(x)
 """

"""#Built-In Modules

import  platform

x = platform.system()
#y = dir(platform)



print(x)
print(y)
"""

"""#Dates
import datetime

#x = datetime.datetime.now()
#print(x.year)                                    #Year
#print(x.strftime("%A"))                      #Day name, %a for short version

x = datetime.datetime(2022,1,15)
print(x)
print(x.strftime("%B"))                     #Year Name,  %b  for short version
"""
