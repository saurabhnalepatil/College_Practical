#Program to implement function programing function such as filter and reduce

#importing reduce to use in program
from functools import reduce


list2=[10,2,5,4,32,12,69,19,53,47,34,35,22,14,5,89]

def func(x):
    if x<=30:
        return x
#using filter function which will filter out less than 30 value
y = filter(func, list2)

print(list(y))



def add(x, y):
    return x + y

#reduce function will do addition of all values
print(reduce(add, list2))


def fun2(s):
    return s[0] == "A"

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
#map function will map true or false accordingly
map_object = map(fun2, fruit)

print(list(map_object))


