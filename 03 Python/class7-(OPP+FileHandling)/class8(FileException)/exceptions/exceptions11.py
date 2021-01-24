print("First")
a = 5
b = 0
d = []
try:
    c = a/b
    e = d[5]
except ZeroDivisionError:
    print("Handel ZeroDivisionError")
except Exception as xyz:
    print("Handle Error", str(xyz))
else:
    print(c)

print("last")

