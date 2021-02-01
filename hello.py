my_fav_things = ["workingout", 356, 45, ["reading", 45]]
print(my_fav_things)

copy = my_fav_things #we are not copying; we are making a new alias
print(copy)

copy[0] = "hangout"
print(my_fav_things)
print(copy)

#to copy a list we can do like this

my_second_fav = ["programming", 344, 566, 67, ["sleeping"]]

second_copy = my_fav_things[:] #By Slicing

#or By using copy() function
# second_copy = my_second_fav.copy()

second_copy[0] = "Development"


print(my_second_fav, second_copy)