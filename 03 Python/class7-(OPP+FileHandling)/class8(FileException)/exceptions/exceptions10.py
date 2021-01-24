print("First")
a = 5
b = 0
d = []
try:
    c = a/b
    
except ZeroDivisionError:
    print("Handel ZeroDivisionError")
except Exception as e:
    print("Handle Error == " +str(e))
else:
    print(c)


try:
    e = d[5]
except Exception as e:
    print("abc==",str(e))
    
    
print("last")

