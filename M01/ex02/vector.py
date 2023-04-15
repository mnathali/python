
class Vector:
    def __init__(self, vect) -> None:
        if isinstance(vect, list) and isinstance(vect[0], list) and bool(len(vect[0])):
            self.values = [[float(x) for x in vect[0]]] if len(vect) == 1 else [[float(x[0])] for x in vect]
            self.shape = (len(vect), len(vect[0]))
            print(1)
        elif isinstance(vect, int):
            self.values = [[float(x)] for x in range(vect)]
            self.shape = (vect, 1)
            print(2)
        elif isinstance(vect, tuple):
            self.values = [[float(x)] for x in range(vect[0], vect[1])]
            self.values = (len(self.values), 1)
            print(3)
        else:
            raise TypeError
        
    def dot(self, other):
        if type(self) != type(other) or self.shape != other.shape:
            raise TypeError
        res = {self.values[0][i]:other.values[0][i] for i in range(self.shape[1])} if \
            self.shape[1] > 1 else {self.values[i][0]:other.values[i][0] for i in range(self.shape[0])}
        return sum([x * y for x,y in res.items()])
    
    def T(self):
        tmp = [[self.values[0][i]] for i in range(self.shape[1])] if self.shape[1] > 1 \
        else [[self.values[i][0] for i in range(self.shape[0])]]
        return Vector(tmp)
    
    def __add__(self, other):
        if type(self) != type(other) or self.shape != other.shape:
            raise TypeError
        res = {self.values[0][i]:other.values[0][i] for i in range(self.shape[1])} if \
            self.shape[1] > 1 else {self.values[i][0]:other.values[i][0] for i in range(self.shape[0])}
        to_ret = [[x + y for x,y in res.items()]] if self.shape[1] > 1 else [[x + y] for x,y in res.items()]
        return Vector(to_ret)
        
    def __radd__(self, oper):
        return self.__add__(oper)
    
    def __sub__(self, other):
        if type(self) != type(other) or self.shape != other.shape:
            raise TypeError
        res = {self.values[0][i]:other.values[0][i] for i in range(self.shape[1])} if \
            self.shape[1] > 1 else {self.values[i][0]:other.values[i][0] for i in range(self.shape[0])}
        to_ret = [[x - y for x,y in res.items()]] if self.shape[1] > 1 else [[x - y] for x,y in res.items()]
        return Vector(to_ret)
        
    def __rsub__(self, oper):
        return self.__sub__(oper)
    
    def __mul__(self, k):
        if not isinstance(k, int) and not isinstance(k, float):
            raise TypeError
        res = [[self.values[0][i] * k for i in range(self.shape[1])]] if self.shape[1] > 1 \
        else [[self.values[i][0] * k] for i in range(self.shape[0])]
        return Vector(res)

    def __rmul__(self, k):
        return self.__mul__(k)

    def __truediv__(self, k):
        if not isinstance(k, int) and not isinstance(k, float):
            raise TypeError
        res = [[self.values[0][i] / k for i in range(self.shape[1])]] if self.shape[1] > 1 \
        else [[self.values[i][0] / k] for i in range(self.shape[0])]
        return Vector(res)
    
    def __rtruediv__(self, k):
        raise ArithmeticError
    
    def __str__(self):
        txt = ("Vector values : " + str(self.values)
               + "\nShape : " + str(self.shape))
        return txt
    
    def __repr__(self):
        txt = str(self.values) + " : " + str(self.shape)
        return txt

  