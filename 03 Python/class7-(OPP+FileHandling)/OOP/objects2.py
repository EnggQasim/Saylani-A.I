class Dog():
    """A simple attempt to model a dog."""

    def __init__(self,name,age):
        print("Dog init")
        print("Name ",name)
        print("Age ", age)
        self.name = name
        self.age = age

    def bark(self):
        print("Dog is barking")

e = Dog("willie",6)

print(e.name)
print(e.age)
e.age = 10
print(e.age)
