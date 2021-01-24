class Dog():
    """A simple attempt to model a dog."""

    def __init__(self,name,age):
        print("Dog init")
        print("Name ",name)
        print("Age ", age)
        self.name = name
        self.age = age

    def bark(self):
        print(self.name +" is barking")

e = Dog("willie",6)
e.bark()