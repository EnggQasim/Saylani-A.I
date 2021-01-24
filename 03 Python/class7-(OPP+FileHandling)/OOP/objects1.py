class Dog():
    """A simple attempt to model a dog."""

    def __init__(self,name,age):
        print("Dog init")
        print("Name ",name)
        print("Age ", age)

    #def __init__(self,name):
    #    print("Dog init")
    #    print("Name ",name)

    def bark(self):
        print("Dog is barking")

e = Dog("willie",6)
#g = Dog("willie")
#print(d)
#d.bark()
