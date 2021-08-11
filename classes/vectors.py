

class vec2:

    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    def get(self):
        return (self.__x,self.__y)

    def set(self,x,y):
        self.__x = x
        self.__y = y

class vec3:

    def __init__(self,x,y,z):
        self.__x = x
        self.__y = y
        self.__z = z

    def get(self):
        return (self.__x,self.__y,self.__z)

    def set(self,x,y,z):
        self.__x = x
        self.__y = y
        self.__z = z

class vec4:

    def __init__(self,x,y,z,w):
        self.__x = x
        self.__y = y
        self.__z = z
        self.__w = w

    def get(self):
        return (self.__x,self.__y,self.__z,self.w)

    def set(self,x,y,z,w):
        self.__x = x
        self.__y = y
        self.__z = z
        self.__w = w