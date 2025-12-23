from copy import deepcopy


# Type dList:
# A dList is a simple linked list allowing declarative programming.
# The two central data structures are dLists consisting of an
# element (car) and a dList (cdr).
# car: the head of the list
# cdr: the rest of the list
# To identify the end of a list a data structure called emptyDList is used.
# Example: The python list [1,2,3] is mapped in symbols to a dList
# 1 -> 2 -> 3 -> emptyDList
# The abstract base class dListTool implements all usually needed methods to work with simple linked lists.

class dList:
    pass


class emptyDList(dList):
    def __init__(self):
        pass


class dPair(dList):
    car = None
    cdr = None

    def __init__(self, aCar, aCdr):
        self.car = aCar
        self.cdr = aCdr


def makeEmptyDList():
    return emptyDList()


def cons(e, l: dList):
    return dPair(deepcopy(e), deepcopy(l))


# Prädikate
def isEmptyDList(l):
    return isinstance(l, emptyDList)


def isDPair(l):
    return isinstance(l, dPair)


def isDList(l):
    return isinstance(l, dList)


def getCar(l: dList):
    if isinstance(l, emptyDList):
        print("!!! Type-Error !!!")
        return None
    elif isinstance(l, dPair):
        return deepcopy(l.car)


def getCdr(l: dList):
    if isinstance(l, emptyDList):
        print("!!! Type-Error !!!")
    elif isinstance(l, dPair):
        return deepcopy(l.cdr)


def getElement(l: dList, pos: int):
    if isEmptyDList(l):
        print("!!! Error in method getEntry !!!")
        return None
    if pos == 0:
        return getCar(l)
    else:
        return getElement(getCdr(l), pos - 1)


def reverse(l: dList, temp=None):
    if temp is None:
        temp = emptyDList()
    if isEmptyDList(l):
        return temp
    if isDPair(l):
        return reverse(getCdr(l),
                       cons(getCar(l), temp)
                       )


def makeDListFromList(l: list):
    ret = makeEmptyDList()
    for x in l:
        ret = cons(x, ret)
    return reverse(ret)


# Ausgabe
def myPrint(l):  # <----------------------------- rename
    if isEmptyDList(l):
        return
    else:
        print(getCar(l))
        myPrint(getCdr(l))


# Weitere Methoden

def len(l, akk=0):
    if isEmptyDList(l):
        return akk
    else:
        return len(getCdr(l), akk + 1)


def append(l, m, temp=None):
    if temp is None:
        temp = reverse(l)
    if isEmptyDList(m):
        return reverse(temp)
    else:
        return append(l, getCdr(m), cons(getCar(m), temp))


def insertEntry(e, l, pos, temp=None):
    if isEmptyDList(l):
        print("!!! Error in method setEntry !!!")
        return None

    if temp is None:
        temp = emptyDList()

    if pos == 0:
        return append(reverse(temp), cons(e, l))

    else:
        return insertEntry(e,
                           getCdr(l),
                           pos - 1,
                           cons(getCar(l), temp))


def map(f, l, temp=None):
    if temp is None:
        temp = emptyDList()
    if isEmptyDList(l):
        return reverse(temp)
    else:
        return map(f, getCdr(l),
                   cons(f(getCar(l)),
                        temp))


# Example

def run():
    print(isinstance([1, 2, 3], list))
    print(type([1, 2, 3]))

    print()
    x = cons(2, cons(1, emptyDList()))
    myPrint(x)

    print()
    y = makeDListFromList([1, 2, 3, 4, 5])
    myPrint(y)

    print()
    print(len(y))

    print()
    print(getElement(y, 0))
    print(getElement(y, 1))

    print()
    myPrint(reverse(y))

    print()
    print("Append")
    myPrint(x)
    myPrint(y)
    myPrint(append(x, y))

    print()
    print("setEntry")
    myPrint(insertEntry('a', y, 3))

    print()
    print("map")

    def f(x):
        return x + 1

    myPrint(map(f, y))


run()

# todos
# removeEntry
# filter
# sort
# fold
