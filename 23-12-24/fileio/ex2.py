file=open("one.txt","a")
file.write("Hello")
file.write("World")
file2=open("one.txt","r")
print(file2.readline())
print(file2.readline())