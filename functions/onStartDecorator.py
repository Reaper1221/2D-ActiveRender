import numpy as np

onStartFunc = [] # Хранит функции которые исполняются при старе
onStartFuncArgs = [] # Хранит аргументы функций которые исполняются при старте

 # Декоратор метода Start, нужен для функции которая будет срабатывать при старте проекта
def onStart(args = ()):

    def func(func):

        def a():

            onStartFunc.append(func)
            onStartFuncArgs.append(args)

            return func(args)

        return a

    return func