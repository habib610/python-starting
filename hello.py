#deep copy

# fav_food = ["banana", "chicken", ["burger", "pizza"]]
# copy = fav_food.copy()

# copy[1] = "role"

# print(fav_food, "\n", copy)

# shallow copy works by using copy method; But when you go for deep copy like nested list this wont work then import copy 


import copy

fav_food = ["banana", "chicken", ["burger", "pizza"]]
c = copy.deepcopy(fav_food)
c[2][0] = "role"

print(fav_food, "\n", c)