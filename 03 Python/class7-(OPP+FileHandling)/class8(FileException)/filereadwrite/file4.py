mylist = ["hello","test"]
with open('demo.txt') as fileObj:
    lines = fileObj.readlines()
    mylist  = mylist + lines
    print(mylist)