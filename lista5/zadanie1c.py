#Wariant C
class Wyrazenie:
    def __add__(self,arg):
        return Dodaj(self,arg)
    def __mul__(self,arg):
        return Razy(self,arg)
    def __div__(self,arg):
        return Dziel(self,arg)
    def __sub__(self,arg):
        return Odejmij(self,arg)


class Stala(Wyrazenie):
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return str(self.val)
    def oblicz(self,zmienne):
        return self.val


class Zmienna(Wyrazenie):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return str(self.name)
    def oblicz(self,zmienne):
        if self.name not in zmienne:
            raise VariableNotFoundException()
        return zmienne[self.name]


class Razy(Wyrazenie):
    def __init__(self, l, p):
        self.l = l
        self.p = p
    def __str__(self):
        return '(' + str(self.l) + ' * ' + str(self.p) + ')'
    def oblicz(self, zmienne):
        return self.l.oblicz(zmienne) * self.p.oblicz(zmienne)


class Dodaj(Wyrazenie):
    def __init__(self, l, p):
        self.l = l
        self.p = p
    def __str__(self):
        return '(' + str(self.l) + ' + ' + str(self.p) + ')'
    def oblicz(self, zmienne):
        return self.l.oblicz(zmienne) + self.p.oblicz(zmienne)


class Odejmij(Wyrazenie):
    def __init__(self, l, p):
        self.l = l
        self.p = p
    def __str__(self):
        return '(' + str(self.l) + ' - ' + str(self.p) + ')'
    def oblicz(self, zmienne):
        return self.l.oblicz(zmienne) - self.p.oblicz(zmienne)


class Dziel(Wyrazenie):
    def __init__(self, l, p):
        self.l = l
        self.p = p
    def __str__(self):
        return '(' + str(self.l) + ' / ' + str(self.p) + ')'
    def oblicz(self, zmienne):
        if self.p.oblicz(zmienne) == 0:
            raise DivisionByZeroException()
        return self.l.oblicz(zmienne) / self.p.oblicz(zmienne)


class Pochodna(Wyrazenie):
    def __init__(self, wyr):
        self.wyr = wyr
    def __str__(self):
        return str(self.wyr) + '\''
    def oblicz(self, zmienne):
        if isinstance(self.wyr, Stala):
            return Stala(0)
        elif isinstance(self.wyr, Zmienna):
            return Stala(1)
        elif isinstance(self.wyr, Razy):
            return Dodaj(Razy(Pochodna(self.wyr.l).oblicz(zmienne), self.wyr.p), Razy(self.wyr.l, Pochodna(self.wyr.p).oblicz(zmienne)))
        elif isinstance(self.wyr, Dodaj):
            return Dodaj(Pochodna(self.wyr.l).oblicz(zmienne), Pochodna(self.wyr.p).oblicz(zmienne))
        elif isinstance(self.wyr, Odejmij):
            return Odejmij(Pochodna(self.wyr.l).oblicz(zmienne), Pochodna(self.wyr.p).oblicz(zmienne))
        elif isinstance(self.wyr, Dziel):
            return Dziel(Odejmij(Razy(Pochodna(self.wyr.l).oblicz(zmienne), self.wyr.p), Razy(self.wyr.l, Pochodna(self.wyr.p).oblicz(zmienne))), Razy(self.wyr.p, self.wyr.p))


class DivisionByZeroException(Exception):
    pass

class VariableNotFoundException(Exception):
    pass

#TESTY
zmienne = { 'x': 1, 'y': 2, 'z':3}

t1 = Dodaj(Dziel(Stala(6),Zmienna("y")),Odejmij(Stala(7),Zmienna("z")))
print(t1.__str__())
print(t1.oblicz(zmienne))
print()

t2 = Odejmij(Razy(Dodaj(Stala(5),Zmienna("x")),Dziel(Stala(12),Zmienna("z"))),Stala(7))
print(t2.__str__())
print(t2.oblicz(zmienne))
print()

t3 = Dziel(Razy(t1,t2),Dodaj(t1,t2))
print(t3.__str__())
print(t3.oblicz(zmienne))
print()

t4 = Pochodna(t1)
print(t4.__str__())
print(t4.oblicz(zmienne))
print()

t5= Pochodna(Razy(Dodaj(Zmienna('x'), Stala(2)), Odejmij(Zmienna('z'), Stala(4))))
print(t5.__str__())
print(t5.oblicz(zmienne))
print()

"""
t6= Dziel(Zmienna("x")/Stala(0))
print(t6.__str__())
print(t6.oblicz(zmienne))

t7= Dziel(Zmienna("v")/Stala(3))
print(t7.__str__())
print(t7.oblicz(zmienne))
"""






