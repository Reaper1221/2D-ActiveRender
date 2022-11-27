# Классы векторов для упрощения работы с движком

class Vec2:

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get(self):
        return (self._x, self._y)

    def set(self, sc):
        if isinstance(sc, type((1,1,1,1))):
            self._x = sc[0]
            self._y = sc[1]
        elif isinstance(sc, Vec2):
            self._x = sc._x
            self._y = sc._y

    def __add__(self, other):
        if isinstance(other, Vec2):
            sc = other
            return Vec2(self._x + sc._x, self._y + sc._y)
        elif isinstance(other, type((1,1,1,1))):
            sc = other
            return Vec2(self._x + sc[0], self._y + sc[1])
        else: raise ArithmeticError("Data error, Vec2 data only.")

    def __sub__(self, other):
        if isinstance(other, Vec2):
            sc = other
            return Vec2(self._x - sc._x, self._y - sc._y)
        elif isinstance(other, type((1,1,1,1))):
            sc = other
            return Vec2(self._x - sc[0], self._y - sc[1])
        else: raise ArithmeticError("Data error, Vec2 data only.")

    def __mul__(self, other):
        if isinstance(other, Vec2):
            sc = other
            return Vec2(self._x * sc._x, self._y * sc._y)
        elif isinstance(other, type((1,1,1,1))):
            sc = other
            return Vec2(self._x * sc[0], self._y * sc[1])
        else: raise ArithmeticError("Data error, Vec2 data only.")

    def __truediv__(self, other):
        if isinstance(other, Vec2):
            sc = other
            return Vec2(self._x / sc._x, self._y / sc._y)
        elif isinstance(other, type((1,1,1,1))):
            sc = other
            return Vec2(self._x / sc[0], self._y / sc[1])
        else: raise ArithmeticError("Data error, Vec2 data only.")
    
    def __floordiv__(self, other):
        if isinstance(other, Vec2):
            sc = other
            return Vec2(self._x // sc._x, self._y // sc._y)
        elif isinstance(other, type((1,1,1,1))):
            sc = other
            return Vec2(self._x // sc[0], self._y // sc[1])
        else: raise ArithmeticError("Data error, Vec2 data only.")

    def __mod__(self, other):
        if isinstance(other, Vec2):
            sc = other
            return Vec2(self._x % sc._x, self._y % sc._y)
        elif isinstance(other, type((1,1,1,1))):
            sc = other
            return Vec2(self._x % sc[0], self._y % sc[1])
        else: raise ArithmeticError("Data error, Vec2 data only.")

class Vec3:

    def __init__(self, x=0, y=0 ,z=0):
        self._x = x
        self._y = y
        self._z = z

    def get(self):
        return (self._x, self._y, self._z)

    def set(self, sc):
        if isinstance(sc, type((1,1,1,1))):
            self._x = sc[0]
            self._y = sc[1]
            self._z = sc[2]
        elif isinstance(sc, Vec3):
            self._x = sc._x
            self._y = sc._y
            self._z = sc._z

    def __add__(self, other):
        if isinstance(other, Vec3):
            sc = other
            return Vec3(self._x + sc._x, self._y + sc._y, self._z + sc._z)
        elif isinstance(other, type((1,1,1,1))):
            sc = other
            return Vec3(self._x + sc[0], self._y + sc[1], self._z + sc[2])
        else: raise ArithmeticError("Data error, Vec3 data only.")

    def __sub__(self, other):
        if isinstance(other, Vec3):
            sc = other
            return Vec3(self._x - sc._x, self._y - sc._y, self._z - sc._z)
        elif isinstance(other, type((1,1,1,1))):
            sc = other
            return Vec3(self._x - sc[0], self._y - sc[1], self._z - sc[2])
        else: raise ArithmeticError("Data error, Vec3 data only.")

    def __mul__(self, other):
        if isinstance(other, Vec3):
            sc = other
            return Vec3(self._x * sc._x, self._y * sc._y, self._z * sc._z)
        elif isinstance(other, type((1,1,1,1))):
            sc = other
            return Vec3(self._x * sc[0], self._y * sc[1], self._z * sc[2])
        else: raise ArithmeticError("Data error, Vec3 data only.")

    def __truediv__(self, other):
        if isinstance(other, Vec3):
            sc = other
            return Vec3(self._x / sc._x, self._y / sc._y, self._z / sc._z)
        elif isinstance(other, type((1,1,1,1))):
            sc = other
            return Vec3(self._x / sc[0], self._y / sc[1], self._z / sc[2])
        else: raise ArithmeticError("Data error, Vec3 data only.")
    
    def __floordiv__(self, other):
        if isinstance(other, Vec3):
            sc = other
            return Vec3(self._x // sc._x, self._y // sc._y, self._z // sc._z)
        elif isinstance(other, type((1,1,1,1))):
            sc = other
            return Vec3(self._x // sc[0], self._y // sc[1], self._z // sc[2])
        else: raise ArithmeticError("Data error, Vec3 data only.")

    def __mod__(self, other):
        if isinstance(other, Vec3):
            sc = other
            return Vec3(self._x % sc._x, self._y % sc._y, self._z % sc._z)
        elif isinstance(other, type((1,1,1,1))):
            sc = other
            return Vec3(self._x % sc[0], self._y % sc[1], self._z % sc[2])
        else: raise ArithmeticError("Data error, Vec3 data only.")

class Vec4:

    def __init__(self, x=0, y=0, z=0, w=0):
        self._x = x
        self._y = y
        self._z = z
        self._w = w

    def get(self):
        return (self._x, self._y, self._z, self._w)

    def set(self, sc):
        if isinstance(sc, type((1,1,1,1))):
            self._x = sc[0]
            self._y = sc[1]
            self._z = sc[2]
            self._w = sc[3]
        elif isinstance(sc, Vec4):
            self._x = sc._x
            self._y = sc._y
            self._z = sc._z
            self._w = sc._w

    def __add__(self, other):
        if isinstance(other, Vec4):
            sc = other
            return Vec4(self._x + sc._x, self._y + sc._y, self._z + sc._z, self._w + sc._w)
        elif isinstance(other, type((1,1,1,1))):
            sc = other
            return Vec4(self._x + sc[0], self._y + sc[1], self._z + sc[2], self._w + sc[3])
        else: raise ArithmeticError("Data error, Vec4 data only.")

    def __sub__(self, other):
        if isinstance(other, Vec4):
            sc = other
            return Vec4(self._x - sc._x, self._y - sc._y, self._z - sc._z, self._w - sc._w)
        elif isinstance(other, type((1,1,1,1))):
            sc = other
            return Vec4(self._x - sc[0], self._y - sc[1], self._z - sc[2], self._w - sc[3])
        else: raise ArithmeticError("Data error, Vec4 data only.")

    def __mul__(self, other):
        if isinstance(other, Vec4):
            sc = other
            return Vec4(self._x * sc._x, self._y * sc._y, self._z * sc._z, self._w * sc._w)
        elif isinstance(other, type((1,1,1,1))):
            sc = other
            return Vec4(self._x * sc[0], self._y * sc[1], self._z * sc[2], self._w * sc[3])
        else: raise ArithmeticError("Data error, Vec4 data only.")

    def __truediv__(self, other):
        if isinstance(other, Vec4):
            sc = other
            return Vec4(self._x / sc._x, self._y / sc._y, self._z / sc._z, self._w / sc._w)
        elif isinstance(other, type((1,1,1,1))):
            sc = other
            return Vec4(self._x / sc[0], self._y / sc[1], self._z / sc[2], self._w / sc[3])
        else: raise ArithmeticError("Data error, Vec4 data only.")
    
    def __floordiv__(self, other):
        if isinstance(other, Vec4):
            sc = other
            return Vec4(self._x // sc._x, self._y // sc._y, self._z // sc._z, self._w // sc._w)
        elif isinstance(other, type((1,1,1,1))):
            sc = other
            return Vec4(self._x // sc[0], self._y // sc[1], self._z // sc[2], self._w // sc[3])
        else: raise ArithmeticError("Data error, Vec4 data only.")

    def __mod__(self, other):
        if isinstance(other, Vec4):
            sc = other
            return Vec4(self._x % sc._x, self._y % sc._y, self._z % sc._z, self._w % sc._w)
        elif isinstance(other, type((1,1,1,1))):
            sc = other
            return Vec4(self._x % sc[0], self._y % sc[1], self._z % sc[2], self._w % sc[3])
        else: raise ArithmeticError("Data error, Vec4 data only.")