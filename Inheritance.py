fruits = ["fruit", "apple", "lithci", "banana"]
# print(fruits)

fruits.insert(2, "newFood")
# print(fruits)

def funList(*args):
    args = list(args)
    return  args

li = funList("bangladesh", "myanmar", "vutan", "pakistam")
print(li)