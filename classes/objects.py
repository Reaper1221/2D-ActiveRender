import numpy as np
from . import prefabs

MINIMAL = -100000000000000000000000000000000000000000

class Objects:

    Screen_pointers = np.array([[MINIMAL,MINIMAL],[MINIMAL,MINIMAL]])

    def __init__(self, engine):
        self.Screen_pointers = np.array([[MINIMAL,MINIMAL], [MINIMAL,MINIMAL]]) # В данном масиве хранять все координаты точек на экране
        self.Screen_pointers_ID_em = [] # В этом масиве храниться количевстве точек пренадлежащуищие определённому объекту
        self.move_bool = engine.get_movevment()
        self.del_objects = engine.get_delete()

    # Движение объекта по заданым координатам ( в разработке )
    def move_obj(self, indexobject: int, x=0, y=0, ): 
        if self.move_bool:

            index = 0
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

    def _set_points(self, points) -> None:
        self.Screen_pointers = points

    def del_obj(self, indexobject: int): 
        if self.del_objects:
            index = 0
            move = False

            c = 0
            ix = 0
            
            if len(self.Screen_pointers_ID_em) != 0: self.Screen_pointers_ID_em = np.delete(self.Screen_pointers_ID_em, indexobject)

            for b in range(len(self.Screen_pointers)):
                if not move:
                    if indexobject == 0: move = True
                    elif type(self.Screen_pointers[b, 0]) == type(str()) and type(self.Screen_pointers[b, 1]) == type(str()):
                        if index == indexobject:
                            move = True
                            c = b
                        else: index = index + 1
                elif move: 
                    ix = ix + 1
                    if type(self.Screen_pointers[b, 0]) == type(str()) and type(self.Screen_pointers[b, 1]) == type(str()): break
                    
            for x in range(ix):  self.Screen_pointers = np.delete(self.Screen_pointers, c, axis=0)

    def del_all_obj(self):
        self.Screen_pointers = np.array([[MINIMAL,MINIMAL],[MINIMAL,MINIMAL]])

    def get(self, indexobject: int): 

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

    def get_all(self):
        return self.Screen_pointers

    # Ошибка не верного результата функции декоратора CreateObject
    def __DecoratorObjectError(self, func_name: str):
        print(f"ФАТАЛЬНАЯ ОШИБКА: ФУНКЦИЯ {func_name} = ВЕРНУЛА НЕ ВЕРНЫЙ МАССИВ NUMPY!")
        print("ПРИМЕР ВЫВОДА: [[1, 1], [1, 2], [2, 1], [2, 2]]")
        print("ПЕРВАЯ ЦИФРА ЭТО X ВТОРАЯ ЭТО Y")
        exit()

    # Инициализация префаба
    def init_prefab(self, prefab: prefabs.Prefab):
        result = prefab.get()
        result = np.append(result, [["END__OBJECT","END__OBJECT"]], axis=0)
        self.Screen_pointers = np.append(self.Screen_pointers, result ,axis=0)

    # Данный декоратор нужен для создания объектов.
    def createObject(self, *args, **kargs):
        def func(func):
        
            def a(*args, **kargs):
         
                result = func(*args, **kargs)
                points = 2

                self.Screen_pointers_ID_em.append(len(result))
         
                if type(result) != type(np.array([])):
                    self.__DecoratorObjectError(str(func.__name__))
                else:
                    for x in range(len(result)): 
                        if type(result[x-1]) != type(np.array([])): self.__DecoratorObjectError(str(func.__name__))
                    
                self.Screen_pointers = np.append(self.Screen_pointers, np.append(result, [["END__OBJECT","END__OBJECT"]], axis=0),axis=0) # [0][0][0][0]
                
                return result
            
            return a
        
        return func