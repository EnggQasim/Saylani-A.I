class Student():
    def __init__(self,name,age):
        if age > 80 or age <16:
            raise Exception("Age can not be greater then 80 and less then 16")
        self.name = name
        self.age = age

print("before")
st = Student("Hello",81)
print(st.age)

print("after")