print("First")
a = 5
b = 2
d = []
try:
    'abc' + 5
    c = a/b
    f = d[5]
except Exception as e:
    print("Handle Error == " + str(e))
else:
    print(c)

print("last")

