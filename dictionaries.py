band = {
    "vocals": "Me",
    "guitar": "Him"
}
band2 = dict(vocals = "Me 1", guitar = "Him 1")


print(band)
print(band2)
print(type(band))
print(len(band2))


#Access items
print(band["guitar"], band["vocals"])
print(band.get("vocals"))

#list all keys
print(band.keys())

#list all values
print(band.values())

#list of (key/value) pairs as tuples
print(band.items())


#verify a key exists
print("guitar" in band)
print("something" in band)


#Change values
band["vocals"] = "Kelvin Ward"
band.update({"bass": "Tyler"})
print(band)


#Remove items
print(band.pop("bass"))
print(band)


band["drums"] = "Ok boham"
print(band)


print(band.popitem())
print(band)


#Delete and clear
band["drums"] = "Ok boham"
del band["drums"]
print(band)


band2.clear()
print(band2)

del band2


#Copy dictionary

# band2 = band #create a reference
# print("Bad copy!")
# print(band2)


# band2["drums"] = "Tyler HAHA"
# print(band2)

band2 = band.copy()
band2["drums"] = "Tyler"
print(band2, band)

#or use the dict() constructor function

band3 = dict(band)
print("Good copy!")
print(band3)


#Nested dictionary
member1 = {
    "name": "Kelvin",
    "age": 28,
}

member2 = {
    "name": "Fuck",
    "age": 24,
}

bandOther = {
    "member1": member1,
    "member2": member2
}

print(bandOther)
print(bandOther["member1"])
print(bandOther["member1"]["name"])


#Set

nums = {1,2,3,4}
nums1 = set((1,2,3,4))

print(nums)
print(nums1)
print(type(nums))
print(len(nums))


#No duplicate allowed

numsOther = {1,2,3,4,4,5}
print(numsOther)

#True is a dupe of 1, False is a dupe of zero

nums = {1,True,2,False,3,4,5}
print(nums)

#Check if a value in a set
print(2 in nums)


#But you cannot refer to an elemt in the set with an index possition or a key
#Add a new element to a set
nums.add(8)
print(nums)

#Add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

#you can update with lists, tuples and dictionaries too

#Merge two sets to create a new set
one = {1,2,3}
two = {4,5,6}

mynewset = one.union(two)
print(mynewset)

#Keep onely the duplicates
three = {7,8,9}
four = {9,10,12}

three.intersection_update(four)
print(three)

#Keep everything except the duplicates
three = {7,8,9}
four = {9,8,12}

three.symmetric_difference_update(four)
print(three)