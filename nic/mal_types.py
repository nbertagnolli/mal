class List(list):
    def __add__(self, rhs):
        return List(list.__add__(self, rhs))

    def __getitem__(self, i):
        if type(i) == slice:
            return List(list.__getitem__(self, i))
        elif i >= len(self):
            return None
        else:
            return list.__getitem__(self, i)

    def append(self, rhs):
        return self.__add__([rhs])

    def __getslice__(self, *a):
        return List(list.__getslice__(self, *a))

class Symbol(str):
    pass

class Number():
    pass