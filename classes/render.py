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

        self.render_calls = 0 # Хранит количевство вызовов рендера
        self.render_time = 0 # Хранит длительность последний отрисовки
        self.onRenderFunc = []
        self.onRenderFuncArgs = []
        self.animate_cadr = [] # Кадры для анимации
        self.debug = False # дебан мод, только для двух поточного рендера

        self.__EmptyScreen() # создания пустого дисплея
        
        # Не вдавайтесь в подробности как это работает...

    # Он очищает дисплей.
    def __EmptyScreen(self):
        scx = np.array([])
        sc = np.array([])
        
        for x in range(self.withd):     
            scx = np.append(scx, [" "])

        for y in range(self.height):
            sc = np.append(sc, [scx])

        self.Screen = sc

    def QuadRender(self, objects):

        if len(objects.Screen_pointers) % 2 == 1: objects.Screen_pointers = np.append(objects.Screen_pointers, [[MINIMAL,MINIMAL]], axis=0)

        t = time.time()

        self.__EmptyScreen()

        args_point = 0
        if len(self.onRenderFunc) != 0: 
            for func in self.onRenderFunc:
                func(self.onRenderFuncArgs[args_point])
                args_point = args_point + 1

        def duoThread(self, objects):

            u = int(len(objects.Screen_pointers)/4)

            for b in range(u):
            
                if type(objects.Screen_pointers[b-1+u,  0]) != type(str()) and type(objects.Screen_pointers[b-1, 1]) != type(str()):
                    x = objects.Screen_pointers[b-1+u,  0] - 1
                    y = objects.Screen_pointers[b-1+u,  1] - 1


                    if x < self.withd and y < self.height and x >= 0 and y >= 0: 
                        self.Screen[int(y * self.withd + x - 1)] = self.objectSymbol

        def oneThread(self, objects):

            u = int(len(objects.Screen_pointers)/4)

            for b in range(u):
                
                if type(objects.Screen_pointers[b-1, 0]) != type(str()) and type(objects.Screen_pointers[b-1+u, 1]) != type(str()):
                    x = objects.Screen_pointers[b-1, 0] - 1
                    y = objects.Screen_pointers[b-1, 1] - 1


                    if x < self.withd and y < self.height and x >= 0 and y >= 0: 
                        self.Screen[int(y * self.withd + x - 1)] = self.objectSymbol

        def ThreeThread(self, objects):

            u = int(len(objects.Screen_pointers)/4)

            for b in range(u):
            
                if type(objects.Screen_pointers[b-1+u*2,  0]) != type(str()) and type(objects.Screen_pointers[b-1, 1]) != type(str()):
                    x = objects.Screen_pointers[b-1+u*2,  0] - 1
                    y = objects.Screen_pointers[b-1+u*2,  1] - 1


                    if x < self.withd and y < self.height and x >= 0 and y >= 0: 
                        self.Screen[int(y * self.withd + x - 1)] = self.objectSymbol

        def FourThread(self, objects):

            u = int(len(objects.Screen_pointers)/4)

            for b in range(u):
                
                if type(objects.Screen_pointers[b-1+u*3,  0]) != type(str()) and type(objects.Screen_pointers[b-1, 1]) != type(str()):
                    x = objects.Screen_pointers[b-1+u*3,  0] - 1
                    y = objects.Screen_pointers[b-1+u*3,  1] - 1


                    if x < self.withd and y < self.height and x >= 0 and y >= 0: 
                        self.Screen[int(y * self.withd + x - 1)] = self.objectSymbol

        FourRenders = tr.Thread(target=FourThread, args=(self, objects))
        FourRenders.start()
        ThreeRenders = tr.Thread(target=ThreeThread, args=(self, objects))
        ThreeRenders.start()
        duoRenders = tr.Thread(target=duoThread, args=(self, objects))
        duoRenders.start()
        oneRenders = tr.Thread(target=oneThread, args=(self, objects))
        oneRenders.start()
            

        self.render_calls = self.render_calls + 1
        oneRenders.join()

        d = ""
        for x in range(len(self.Screen)):
            d = d + str(self.Screen[x-1])
        print(d)
        self.render_time = time.time() - t


    def duoRender(self, objects):

        t3 = time.time()
        if len(objects.Screen_pointers) % 2 == 1: objects.Screen_pointers = np.append(objects.Screen_pointers, [[MINIMAL,MINIMAL]], axis=0)
        t3 = time.time() - t3

        t = time.time()

        t5 = time.time()
        self.__EmptyScreen()
        t5 = time.time() - t5

        t4 = time.time()
        args_point = 0
        if len(self.onRenderFunc) != 0: 
            for func in self.onRenderFunc:
                func(self.onRenderFuncArgs[args_point])
                args_point = args_point + 1
        t4 = time.time() - t4

        
        
        def oneThread(self, objects):
            u = int(len(objects.Screen_pointers)/2)

            for b in range(int(len(objects.Screen_pointers)/2)):
                
                if type(objects.Screen_pointers[b-1+u, 0]) != type(str()) and type(objects.Screen_pointers[b-1+u, 1]) != type(str()):
                    x = objects.Screen_pointers[b-1+u, 0] - 1
                    y = objects.Screen_pointers[b-1+u, 1] - 1


                    if x < self.withd and y < self.height and x >= 0 and y >= 0: 
                        self.Screen[int(y * self.withd + x - 1)] = self.objectSymbol
        
        
        oneRenders = tr.Thread(target=oneThread, args=(self, objects))
        t1 = time.time()
        oneRenders.start()

        t2 = time.time()

        for b in range(int(len(objects.Screen_pointers)/2)):
        
            if type(objects.Screen_pointers[b-1, 0]) != type(str()) and type(objects.Screen_pointers[b-1, 1]) != type(str()):
                x = objects.Screen_pointers[b-1, 0] - 1
                y = objects.Screen_pointers[b-1, 1] - 1


                if x < self.withd and y < self.height and x >= 0 and y >= 0: 
                    self.Screen[int(y * self.withd + x - 1)] = self.objectSymbol
        
        t2 = time.time() - t2

        oneRenders.join() 
        t1 = time.time() - t1

        t6 = time.time()

        d = ""
        for x in range(len(self.Screen)):
            d = d + str(self.Screen[x-1])

        t6 = time.time() - t6
        self.render_time = time.time() - t
        self.render_calls = self.render_calls + 1

        if self.debug:
            print(f"==========================================\n")
            print(f"{t1} = one\n")
            print(f"==========================================\n")
            print(f"{t2} = two\n")
            print(f"==========================================\n")
            print(f"{t1 - t2} = |one - two|\n")
            print(f"==========================================\n")
            print(f"{t3} = init cost points\n")
            print(f"==========================================\n")
            print(f"{t4} = @onrender functions\n")
            print(f"==========================================\n")
            print(f"{t5} = cleaning screen\n")
            print(f"==========================================\n")
            print(f"{t6} = print\n")
            print(f"==========================================\n")
            print(f"{len(objects.Screen_pointers)} = points\n")
            print(f"==========================================\n")
            print(f"{self.render_time} = all time render\n")
            print(f"==========================================\n")
        else: print(d)

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

    # Метод старта анимации
    def anim_start(self):
        for x in range(len(self.animate_cadr)):
            time.sleep(1/self.FPS) 
            print(self.animate_cadr[x])

    # Метод анимации (Два потока) изначально рендерит, а при помощи второго метода anim_start(), анимация запускается
    def animate(self, objects):
        
        if len(objects.Screen_pointers) % 2 == 1: objects.Screen_pointers = np.append(objects.Screen_pointers, [[MINIMAL,MINIMAL]], axis=0)

        t = time.time()

        self.__EmptyScreen()

        args_point = 0
        if len(self.onRenderFunc) != 0: 
            for func in self.onRenderFunc:
                func(self.onRenderFuncArgs[args_point])
                args_point = args_point + 1

        def oneThread(self, objects):
            u = int(len(objects.Screen_pointers)/2)

            for b in range(int(len(objects.Screen_pointers)/2)):
                
                if type(objects.Screen_pointers[b-1+u, 0]) != type(str()) and type(objects.Screen_pointers[b-1+u, 1]) != type(str()):
                    x = objects.Screen_pointers[b-1+u, 0] - 1
                    y = objects.Screen_pointers[b-1+u, 1] - 1


                    if x < self.withd and y < self.height and x >= 0 and y >= 0: 
                        self.Screen[int(y * self.withd + x - 1)] = self.objectSymbol

        oneRenders = tr.Thread(target=oneThread, args=(self, objects))
        oneRenders.start()

        for b in range(int(len(objects.Screen_pointers)/2)):
        
            if type(objects.Screen_pointers[b-1, 0]) != type(str()) and type(objects.Screen_pointers[b-1, 1]) != type(str()):
                x = objects.Screen_pointers[b-1, 0] - 1
                y = objects.Screen_pointers[b-1, 1] - 1


                if x < self.withd and y < self.height and x >= 0 and y >= 0: 
                    self.Screen[int(y * self.withd + x - 1)] = self.objectSymbol
            

        self.render_calls = self.render_calls + 1
        oneRenders.join()

        d = ""
        for x in range(len(self.Screen)):
            d = d + str(self.Screen[x-1])

        self.animate_cadr.append(d)
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