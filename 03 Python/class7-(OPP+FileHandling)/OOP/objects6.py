class Dog():
    """A simple attempt to model a dog."""
    total = 0
    def __init__(a,name,age):
        print("Dog init")
        print("Name ",name)
        print("Age ", age)
        a.name = name
        a.age = age
        Dog.total = Dog.total+1

    def bark(b):
        print(b.name +" is barking")

myDog = Dog("willie",6)
yourDog = Dog("lucy",3)

myDog.bark()
yourDog.bark()
print(Dog.total)


