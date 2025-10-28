class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"
    
# Polymorphic function

def animal_sound(animal):
    print(animal.speak())
    
animal_sound(Dog())  # Output: Woof!
animal_sound(Cat())  # Output: Cat!
# ------------------------------------------ #

class Myclass1:
    def show(self):
        print("This is Myclass1")
        
class Myclass2(Myclass1):
    def show(self):
        print("This is Myclass2")

obj=Myclass2()
obj.show()


class Myclass3:
    def show(self,name=None,age=None):
        if name is not None and age is not None:
            print("Hello",name,age)
        elif name is not None:
            print("Hello" ,name)
        elif age is not None:
            print("Hello",age)
        else:
            print("Hello World")
            
obj=Myclass3()
# obj.show()            
# obj.show("Jaffer 23")                      
obj.show(name="Jaffer",age=24) 