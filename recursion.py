def add_one(num):
    if(num >=9):
        return num + 1
    total = num +1
    print(total)
    
    return add_one(total)

# add_one(10)
#mynewtotal = add_one(0)
# print(mynewtotal)


#example
value = True
count = 0
while value:
    count +=1
    #print(value)
    print(count)
    if(count == 5):
        break
    else: 
        value = 0
        continue
    
