import math
#String data type

#literal assignment

first = "Kelvin"
last = "Ward"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))


#contructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

#concatenation
fullname = first + " " + last

# print(fullname)

fullname += "!"

# print(fullname)

#casting a number to a string
decade = str(2001)
# print(type(decade))
# print(decade)

statement = "I like rock music from the " + decade + "s."
# print(statement)

#Mutiple lines
mutiline = '''
    Hey how are you?
    
    I was just cheking in.
                    All good?
'''

# print(mutiline)

#Eascping special characters
sentence = 'I\'m back!\tHey!\nWhat\'s do you think?'
# print(sentence)


#String Method
# print(first)
# print(first.lower())
# print(first.upper())
# print(first)


# print(mutiline.title())
# print(mutiline.replace("good", "Ok"))
# print(mutiline)

# print(len(mutiline))
mutiline += "                        "
mutiline = "          " + mutiline
# print(len(mutiline))

# print(len(mutiline.strip()))
# print(len(mutiline.lstrip()))
# print(len(mutiline.rstrip()))


#Build a menu
title = "menu".upper()
print(title.center(20,"="))
print("Coffee".ljust(16,".") + "$1".rjust(4))
print("Tra Sua".ljust(16,".") + "$2".rjust(4))

print("")

#String index values
# print(first[1])
# print(first[-1])
# print(first[1:-1])
# print(first[1:4])
# print(first[1:])
# print(first[:-1])

#Some methods return boolen data
# print(first.startswith("K"))
# print(first.startswith("W"))
# print(first.endswith("n"))

#Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

#Numeric data types
#interger type
price = 100
best_price = int(50)
# print(type(price))
# print(isinstance(best_price, int))

#float type
gpa = 3.99
y = float(1.55)
# print(type(gpa))
# print(isinstance(gpa, float))

#complex type
comp_value = 5+3j
# print(type(comp_value))
# print(comp_value.real)
# print(comp_value.imag)

#Buil-in functions for numbers

print(abs(gpa))
print(abs(gpa *-1))
print(round(gpa))
print(round(gpa,1))


print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

#Csting s string to a number
zipcoode = "1001"
zip_value = int(zipcoode)
print(type(zip_value))

#Error if you attempt to cast incorrect
# zip_value = int("New")
