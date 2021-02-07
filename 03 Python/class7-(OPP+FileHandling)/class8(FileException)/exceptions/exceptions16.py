class Student():
    def __init__(self,name,age):
        if age > 80 or age <16:
            raise StudentAgeException("Age can not be greater then 80 and less then 16")
        self.name = name
        self.age = age

class StudentAgeException(Exception):
    pass

print("before")
try:
    st = Student("Hello",600)
except StudentAgeException as e:
    print("StudentAgeException == "+str(e))
else :
    print(st.age)

print("after")