class Myclass:
    def __init__(self):
        self.__name="Jaffer"
        print(self.__name)
        
        self.__Show() 
    def __Show(self):
        print("My name is", self.__name)
        
obj=Myclass() 
     
     
class Myclass2:
    def __init__(self):
        self.__name=""
        
    def getname(self):
        return self.__name
    
    def setname(self,name):
        self.__name=name

obj=Myclass2()
obj.setname("Jaffer")
print(obj.getname())    