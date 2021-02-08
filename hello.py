#Sum and fun with range

# ages = list(range(1, 20))
# print(ages)

foods = ["chicken", "burger", "pizza", "sandwitch"]

for food in foods:
    print(food , end=" ")
print()
for i in range(len(foods)):
    print(i, foods[i], end=":::")
