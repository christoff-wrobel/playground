# Beispiel für Call by Object Reference
def learning1():
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

    def cons(e, l):
        print(e)
        print(l)
        return dPair(e, l)

    l = cons("b", "c")
    print(l)
    l2 = cons("a", l)
    l.car = 1  # Hier wird an die Adresse von l geschrieben -> Seiteneffekt
    print(l2.cdr.car)
    print()
    l = cons("d", "e")  # Hier wird eine neue Adresse an l gebunden
    print(l)
    print(l2.cdr)
    print(l2.cdr.car)


learning1()



#Call by object reference
l = [1,2]
# erzeugt eine neue Liste an der Adresse
id(l)

def f(x):
    print(x)
f(l)
# übergibt die Adresse von l an f

l = [3,4]
#erzeugt eine neue Liste an einer anderen Adresse -> kein Seiteneffekt.

l[0] = 1
# Schreibt an die Adresse, die bei l hinterlegt ist -> Seiteneffekt.