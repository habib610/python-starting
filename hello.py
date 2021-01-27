#slice method
#NOTE: starter is always inclusive and starter is always exclusive

one = "0123456789"
print(one[3:]) #inclusive (included the index); output = 3456789

two = "0123456789"
print(two[:4]) #exclusive (doesn't included the index); output = 0123

three = "0123456789"
print(three[3:7])  #included the starter index and excluded outer index; output = 3456

four = "0123456789"
print(four[:-1]) #started from the last index; output = 012345678