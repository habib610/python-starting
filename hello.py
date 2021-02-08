#Conditional
print("whats your age?")
age = int(input())
name = True

if age > 20 or not name:
    print("you are welcome")

elif age == 20 and name:
    print("your age is not enough!")

else: 
    print("Invalid")
