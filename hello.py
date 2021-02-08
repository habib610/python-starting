#Function with unlimited arguments

def greet(*people):
    for person in people:
        print(person, end=" ")
    print()

greet("habib", "rahman", "habibur")

#Function unpacking reverse with unpacking

def greet_unpacking(name, email, id):
    print(name, email, id)

person = ["habib", "habib@mail.com", 5]
greet_unpacking(*person)