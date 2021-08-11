import numpy as np
import time
import threading as tr

MINIMAL = -100000000000000000000000000000000000000000

class Drawer:

    # Конструктор класса. Создание пустого дисплея.
    def __init__(self, withd1=120, height1=30, fps=60, objectSymbol="#") -> None:
     
        self.withd = withd1
        self.height = height1
        self.objectSymbol = str(objectSymbol)
        self.FPS = fps

        global withd, height
        withd,height = withd1, height1

        self.bufer = False
        self.__EmptyScreen() # Создаём пустой дисплей
        self.render_calls = 0 # Хранит количевство вызовов рендера
        self.render_time = 0 # Хранит длительность последний отрисовки
        self.onRenderFunc = []
        self.onRenderFuncArgs = []
        
        # Не в давайтесь в подробности как это работает...


    # Этот метод нужен исключительно для коректной работы класса!
    # Он очищает \ создаёт пустой дисплей.
    def __EmptyScreen(self):

        bufer = np.array([])
        self.Screen = np.array([[]])

        if self.bufer:
            self.Screen = self.__EmptyScreenbufer
        else:
            for x in range(self.withd):     
                bufer = np.append(bufer, ["."])

            for y in range(self.height):
                self.Screen = np.append(self.Screen, [bufer])
            
            self.bufer = True
        
        self.__EmptyScreenbufer = self.Screen


    def duoRender(self, objects):

        if len(objects.Screen_pointers) % 2 == 1: objects.Screen_pointers = np.append(objects.Screen_pointers, [[MINIMAL,MINIMAL]], axis=0)

        t = time.time()

        self.__EmptyScreen()

        args_point = 0
        if len(self.onRenderFunc) != 0: 
            for func in self.onRenderFunc:
                func(self.onRenderFuncArgs[args_point])
                args_point = args_point + 1

        def duoThread(self, objects):
            for b in range(int(len(objects.Screen_pointers)/2)):
            
                if type(objects.Screen_pointers[b-1, 0]) != type(str()) and type(objects.Screen_pointers[b-1, 1]) != type(str()):
                    x = objects.Screen_pointers[b-1, 0] - 1
                    y = objects.Screen_pointers[b-1, 1] - 1


                    if x < self.withd and y < self.height and x >= 0 and y >= 0: 
                        self.Screen[int(y * self.withd + x - 1)] = self.objectSymbol

        def oneThread(self, objects):
            u = int(len(objects.Screen_pointers)/2)

            for b in range(int(len(objects.Screen_pointers)/2)):
                
                if type(objects.Screen_pointers[b-1+u, 0]) != type(str()) and type(objects.Screen_pointers[b-1+u, 1]) != type(str()):
                    x = objects.Screen_pointers[b-1+u, 0] - 1
                    y = objects.Screen_pointers[b-1+u, 1] - 1


                    if x < self.withd and y < self.height and x >= 0 and y >= 0: 
                        self.Screen[int(y * self.withd + x - 1)] = self.objectSymbol

        duoRenders = tr.Thread(target=duoThread, args=(self, objects))
        duoRenders.start()
        oneRenders = tr.Thread(target=oneThread, args=(self, objects))
        oneRenders.start()
            

        self.render_calls = self.render_calls + 1
        oneRenders.join()
        duoRenders.join()

        d = ""
        for x in range(len(self.Screen)):
            d = d + str(self.Screen[x-1])
        print(d)
        self.render_time = time.time() - t

    # Метод обновления экрана
    def render(self, objects):

        t = time.time()

        self.__EmptyScreen()

        args_point = 0
        if len(self.onRenderFunc) != 0: 
            for func in self.onRenderFunc:
                func(self.onRenderFuncArgs[args_point])
                args_point = args_point + 1

        self.render_calls = self.render_calls + 1

        for b in range(int(len(objects.Screen_pointers))):
            
            if type(objects.Screen_pointers[b-1, 0]) != type(str()) and type(objects.Screen_pointers[b-1, 1]) != type(str()):
                x = objects.Screen_pointers[b-1, 0] - 1
                y = objects.Screen_pointers[b-1, 1] - 1


                if x < self.withd and y < self.height and x >= 0 and y >= 0: 
                    self.Screen[int(y * self.withd + x - 1)] = self.objectSymbol


        d = ""
        for x in range(len(self.Screen)):
            d = d + str(self.Screen[x-1])
        print(d)
        self.render_time = time.time() - t

    # Декоратор метода render, нужен для функции которая будет срабатывать при начале отрисовки
    def onRender(self, args):

        def func(func):

            def a():

                self.onRenderFunc.append(func)
                self.onRenderFuncArgs.append(args)

                return func(args)

            return a

        return func