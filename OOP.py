class Myclass:
    name="Jaffer"
    age=23
    
    def Details(self):
        print(f"It's me {self.name} and my age is {self.age} years old")
        
myobj=Myclass()
print(myobj.name)
print(myobj.age)
myobj.Details()
    
class Myclass2:
    def Sum(self, a , b):
        return a+b
myobj2 = Myclass2()
print(myobj2.Sum(30,20))

class Myclass3:
    def __init__(self,name,age):  # python class constructor
        print(f"Name: {name}, Age: {age}")
        
person=Myclass3("Abid",21)


class A:
    def Details_A(self):
        print("Details A")
        
class B:
    def Details_B(self):
        print("Details B")    
         
class C(A,B):
    def Details_C(self):
        print("Details C")
        
myobj3=A()  # Creating an object of class A
myobj3=C()  # Creating an object of class C

myobj3.Details_A() # Inherited from class A
myobj3.Details_B() # Inherited from class B
myobj3.Details_C() # Inherited from class C

        
           
        
           


