person = "Kelvin"
coins = 3

#print("\n" + person + " has " + str(coins) + " coin left.")

message = "\n%s has %s coins left." % (person, coins)
print(message)

message = "\n{} has {} coins left.".format(person, coins)
print(message)

message = "\n{1} has {0} coins left.".format(person, coins)
print(message)


message = "\n{person} has {coins} coins left.".format(person=person, coins=coins)
print(message)

player = {'person': 'Kelvin', 'coins': 3}
message = "\n{person} has {coins} coins left.".format(**player)
print(message)



#f-string this is the way

message = f"\n{person} has {coins} coins left."
print(message)

message = f"\n{person} has {2*5} coins left."
print(message)

message = f"\n{person.lower()} has {2*5} coins left."
print(message)


message = f"\n{player['person']} has {2*5} coins left."
print(message)


#pass formating options

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}")

for num in range(1,11):
    print(f"\n2.25 times {num} is {2.25 * num:.2f}")
    
for num in range(1,11):
    print(f"\n{num} divided by 2.25 is {num / 2.25:.2%}")