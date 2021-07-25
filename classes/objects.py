import numpy as np

MINIMAL = -100000000000000000000000000000000000000000


class Objects:

    Screen_pointers = np.array([[MINIMAL,MINIMAL],[MINIMAL,MINIMAL]])

    def __init__(self):
        self.Screen_pointers = np.array([[MINIMAL,MINIMAL],[MINIMAL,MINIMAL], ["END__OBJECT","END__OBJECT"]]) # В данном масиве хранять все координаты точек на экране
        self.Screen_pointers_ID_em = [] # В этом масиве храниться количевстве точек пренадлежащуищие определённому объекту
        self.Screen_pointers_id = [1] # Этот массив хранит количевство точек до определённого объекта

    # Движение объекта по заданым координатам
    def move(self, indexobject: int, x, y): 

        index = 0
        indexobject = indexobject
        move = False

        for b in range(len(self.Screen_pointers)):
            if not move:
                if type(self.Screen_pointers[b, 0]) == type(str()) and type(self.Screen_pointers[b, 1]) == type(str()):
                    if index == indexobject:
                        move = True
                    else: index = index + 1
            elif move:
                self.Screen_pointers[b, 0] = self.Screen_pointers[b, 0] + x
                self.Screen_pointers[b, 1] = self.Screen_pointers[b, 1] + y
                if type(self.Screen_pointers[b+1, 0]) == type(str()):
                    break


    def get(self, indexobject: int,): 

        index = 0
        indexobject = indexobject
        move = False
        points = np.array([[MINIMAL,MINIMAL], [MINIMAL,MINIMAL]])

        for b in range(len(self.Screen_pointers)):
            if not move:
                if type(self.Screen_pointers[b, 0]) == type(str()) and type(self.Screen_pointers[b, 1]) == type(str()):
                    if index == indexobject:
                        move = True
                    else: index = index + 1
            elif move:
                points = np.append(points, [[self.Screen_pointers[b, 0],self.Screen_pointers[b, 1]]], axis=0)
                if type(self.Screen_pointers[b+1, 0]) == type(str()):
                    break

        return points


    # Ошибка не верного результата функции декоратора CreateObject
    def __DecoratorObjectError(self, func_name: str):
        print(f"ФАТАЛЬНАЯ ОШИБКА: ФУНКЦИЯ {func_name} = ВЕРНУЛА НЕ МАССИВ NUMPY!")
        print("ПРИМЕР ВЫВОДА: [[1, 1], [1, 2], [2, 1], [2, 2]]")
        print("ПЕРВАЯ ЦИФРА ЭТО X ВТОРАЯ ЭТО Y")
        exit()

    # Данный декоратор нужен для создания пользовательских объектов.
    def createObject(self, *args, **kargs):
        def func(func):
        
            def a(*args, **kargs):
         
                result = func(*args, **kargs)
         
                if type(result) != type(np.array([])):
                    self.__DecoratorObjectError(str(func.__name__))
                else:
                    for x in range(len(result)): 
                        if type(result[x-1]) != type(np.array([])): self.__DecoratorObjectError(str(func.__name__))
                    
                self.Screen_pointers = np.append(self.Screen_pointers, np.append(result, [["END__OBJECT","END__OBJECT"]], axis=0),axis=0) # [0][0][0][0]
                
                return result
            
            return a
        
        return func