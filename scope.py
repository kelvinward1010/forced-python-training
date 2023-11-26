

name = "Kelvin"

# def greating(fname):
#     age = 30
#     print(name)
#     print(fname, age)
    
# greating("kelvin")

count = 1

def another():
    age = 30
    #count += 2
    #count = 2
    global count
    count +=2
    def greating(fname):
        nonlocal age
        age = 40
        print(name)
        print(fname, age, count)
    greating("Ward")
    
another()