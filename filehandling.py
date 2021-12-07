"""text = "Think and wonder, wonder and think."

hash_object = hashlib.md5(text.encode())
md5_hash = hash_object.hexdigest()


print(md5_hash)"""
#f = open("/home/prasanna/Documents/python3/python basic/demo.txt", "rt")

#print(f.read())

f = open("demo2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demo2.txt", "r")
print(f.read())

#================================================================open ,write a txt ,close
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())

#to remove 
import os
os.remove("demofile.txt")
import phonenumber
