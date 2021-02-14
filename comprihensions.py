#list compreheensions
li = [1, 2, 3, 4, 5]
li2= [x * x for x in li]
print(li2)

li3 = [x for x in range(1, 6) if x % 2 == 1]
print(li3)