#Sum and fun with range

for i in range(10):
    if i == 9:
        print(i)
    else:
        print(i, end=":::")

print(sum(range(10)))

sum = 0

for i in range(10):
    sum = sum + i

print(sum)
