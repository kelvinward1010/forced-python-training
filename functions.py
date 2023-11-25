def hello_world():
    print("Hello")
    
# hello_world()

def sum(num1=9, num2=3): 
    #print(num1+num2)
    if(type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2

total = sum()
total = sum(7,2)
print(total)

def multiple_items(item1, items2, *items3, **items4):
    print(item1)
    print(type(item1))
    print(items2)
    print(type(items2))
    print(items3)
    print(type(items3))
    print(items4)
    print(type(items4))
    
multiple_items(2,3,"Kelvin", "Justi", name = "Kelvin", fullname = "Kelvin Ward")