saarc = ["Bangladesh", "India", "Pakistan", "Nepal", "Bhutan", "Srilanka", "Afganistan"]
saarc.sort()
# print(saarc)

li = [3, 54,6  ,4 , 3, 54,5, 6,7,7]
li.sort()
# print(li)

li.reverse()
# print(li)

fruits = ["orange", "banana", "mango" ]
fruits.append("litchi")
fruits.insert(2, "jack-fruit")

print(fruits)
fruits.insert(3, "coconut")
print(fruits)

fruits.remove("mango")
print(fruits)

item = "pineapple"

if item in fruits:
    fruits.remove(item)
else:
    print(item, "is not listed")

item2 = fruits.pop(1) #deleting last index or specifc index from list and returns the deleted index
print(item2)
print(fruits)

li3 = [2, 4, 5, 6, 7, 8]
li4 = [9, 10, 11, 12]
li4.extend(li3) # concate two  list
print(li4)

del(li4[1]) #deleting list or specific index value
print(li4)

li5 = []

for x in range(10):
    li5.append(x) #pushing into an empty list
print(li5)

li6 = ["a", "b", "c"]
str2 = "".join(li6) #can make a new string form an list of string
print(str2)

str3 = "::::".join(li6)
print(str3)