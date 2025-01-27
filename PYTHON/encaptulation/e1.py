class person:
    def __init__(self,name,age,gender):
        self.__name=name
        self.__age=age
        self.__gender=gender
    
    @property
    def Name(self):
        return self.__name
    
    @Name.setter
    def Name(self,values):
        self.name=values
    
    @staticmethod
    def myfun():
        print("my function")

p1=person("uday",18,"male")
print(p1.Name)
person.myfun()