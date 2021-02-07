class Student():
    def __init__(self,name,age):
        if age > 80 or age <16:
            raise StudentAgeException("Age can not be greater then 80 and less then 16")
        self.name = name
        self.age = age

class StudentAgeException(Exception):
    pass

print("before")
st = Student("Hello",600)
print(st.age)

print("after")