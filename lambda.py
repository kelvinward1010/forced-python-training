#squared = lambda num: num * num

def squared(num): return num * num

print(squared(3))

addTwo = lambda num: num + 2

print(addTwo(10))


sum = lambda a, b : a + b

print(sum(1,2))


def funcB(x):
    return lambda num : num + x

addTen = funcB(10)
addTwenty = funcB(20)

print(addTen(7))
print(addTwenty(7))



lambda num: num * num

numbers = [1,2,3,4,5,6,7,8,9,10]

squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums))

lambda num: num % 2 != 0

odd_nums = filter(lambda num: num % 2 != 0, numbers)
print(list(odd_nums))


from functools import reduce

lambda acc, curr: acc + curr

numbers2 = [1,2,3,4,5,6,7]

total = reduce(lambda acc, curr: acc + curr, numbers2, 10)

print(total)

print(sum(total, 10))



lambda acc, curr: acc + len(curr)

names = ['Kelvin', "Ward", "Tyler", "Locke"]

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)


print(char_count)