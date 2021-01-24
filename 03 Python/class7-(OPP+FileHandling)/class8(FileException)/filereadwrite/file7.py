
with open('demo1.txt','r+') as fileObj:
    fileObj.write("\nI love programming5!")

    fileObj.seek(0)    
    content = fileObj.readlines()
    print(content)

