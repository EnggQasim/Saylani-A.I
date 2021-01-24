
with open('demo1.txt','a') as fileObj:
    fileObj.write("I love programming!\n")
    content = fileObj.read()
    print(content)