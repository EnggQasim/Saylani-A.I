print("First")
a = 5
b = 5
d = []
try:
    c = a/b
    #e = d[5]
except ZeroDivisionError:
    print("Handel ZeroDivisionError")
except:
    print("Handle Error")
else:
    print(c)
finally:
    print("Finally will always run")

print("last")

