class Student():
    def __init__(self,name,age):
        if age > 80:
            raise Exception("Age can not be greater then 80")
        self.name = name
        self.age = age

print("before")
try:
    st = Student("Hello",600)
    
except Exception as e:
    print("Exception "+str(e))
else :
    print(st.age)

print("after")