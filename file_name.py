import os

f =  open("textfile.txt","x")


f = open("textfile.txt","w")

f.write("hello")    

f = open("textfile.txt","a")

f.write(" world")

f = open("textfile.txt","r")

print(f.read())


f.close()

os.remove("textfile.txt")

