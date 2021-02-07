print("First")
a = 5
b = 5
d = []
try:
    c = a/b
    e = d[5]
except ZeroDivisionError:
    print("Handle ZeroDivisionError")
except IndexError:
    print("Handle IndexError")
else:
    print(c)

print("last")

