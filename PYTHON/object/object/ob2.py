class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("name {}".format(self.name))
        print("age {}".format(self.age))
    def __del__(self):
        print("object deleted")
    def __str__(self):
        return "name {} age {}".format(self.name,self.age)
p1=person("uday",18)
p1.display()
print(p1)