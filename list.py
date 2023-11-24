users = ['Kelvin', "Duy", "Tyler"]
data = ['Dave', 42, True]

emptylist = []

print("Kelvin" in emptylist)
print(users[0])
print(users[-1])

print(users.index('Duy'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))


users.append("HAHAHA")
print(users)

users += ["Duy 2haha"]
print(users)

users.extend(['Jimmy', 'Author'])
print(users)

# users.extend(data)
# print(users)

users[1] = ['Duy copy']
print(users)

users.insert(0, "First List")
print(users)

users[1:3] = ["Replace Another"]
print(users)

users.remove("Tyler")
print(users)

users.pop()
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

users[1:2] = ["kelvin"]
users.sort()
print(users)

users.sort(key=str.lower)
print(users)


users_copy = users.copy()
print(users_copy)



nums = [155,2,3,4,5,6,7,8,9,10,11]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy_specicfic = nums[3:]

print(numscopy)
print(mynums)
mycopy_specicfic.sort()
print(mycopy_specicfic)
print(nums)

print(type(nums))

mylist = list([1,"well", True])
print(mylist)



#Tuples

myTuple = tuple(('Dev', 'Lop', 'Enter', 2, True))
anothorTuple = (1,5,"t")
print(myTuple)
print(type(anothorTuple))

newList = list(myTuple)
newList.append("Ok ")
newTuple = tuple(newList)
print(newTuple)


(one, two, *key) = anothorTuple
print(one, two, *key)

print(anothorTuple.count(1))