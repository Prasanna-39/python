for i in range(6):
    print(i)
    
    # list for loop
print("="*12)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print("="*12)

# break in for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x=="banana":
      break
else:
        print(x,"banana is not their....")
print("="*21)
# continue in for loop 
fruits = ["apple", "banana", "cherry"]
for y in fruits:
   # print(y)
    if y=="banana":
        continue
    print(y)
else:
        print("banana ella ....")
