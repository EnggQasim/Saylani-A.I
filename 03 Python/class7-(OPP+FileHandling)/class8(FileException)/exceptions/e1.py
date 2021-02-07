'''
try -- > وہ کوڈ لکھتے ہیں جس میں error انے کا اندیشہ ہو 
except --> error کی type جو بھی آسکتی یہ ہے
else --َ> code execute if error not accure
finally --> error accure or not this will be run
'''





print("start")

a = 6
b = 0

try:
    c = a/b
except ZeroDivisionError:
    print("آب 0 سے کوئی رقم تقسیم نہیں کر سکتے")
else:
    print(c)
finally:
    print("UIT Students working")




d = [1,3,5]


print("End1")
print("End2")