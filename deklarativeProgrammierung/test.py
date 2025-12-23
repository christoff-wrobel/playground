# Understanding call by object reference:
# python divides data types in mutables and immutables.
#Immutable Built-in Data Types in Python
# Numbers
# Booleans
# Strings
# Bytes
# Tuples
# Mutable Built-in Data Types in Python
# Lists
# Dictionaries
# Sets

# immutable data is passed via call by value
# mutable data is passed via call by reference

lis = [1,2,3,4]
print(lis)
def f(l):
    l[0]="Sideeffect"
    print(l)
f(lis)
print(lis)



print()
lis = [1,2,3,4]
print(lis)
def f(l):
    print(l)
lis[0]="sideeffect"
f(lis)



print()
lis = [1,2,3,4]
print(lis)
def f(l):
    l[0] = "irgendetwas"
    return l
lis2 = f(lis)
lis2[0] = "sideeffect"
print(lis)
print(lis2)


