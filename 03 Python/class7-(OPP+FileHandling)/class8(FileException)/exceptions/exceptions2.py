print("First")
a = 5
b = 2
try:
    c = a/b
    print(c[0])
except ZeroDivisionError:
    print("Handle ZeroDivisionError")
except TypeError:
    print("Type Error...")

print("last")

