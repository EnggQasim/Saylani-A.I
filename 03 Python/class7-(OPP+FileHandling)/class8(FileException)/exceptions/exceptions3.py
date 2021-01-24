print("First")
a = 5
b = 0
try:
    c = a/b
    
except (ZeroDivisionError, TypeError):
    print("We are trying to solve problem")
else:
    print(c)

print("last")

