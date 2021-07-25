import numpy as np

onUpdateFunc = [] # Хранит функцию которая запускается при начале рендеринга
onUpdateFuncArgs = [] # Хранит аргументы тех самых функций

# Декоратор метода Update, нужен для кастомной функции, которая будет срабатывать сразу при рендеринге
def onUpdate(args = ()):

    def func(func):

        def a():

            onUpdateFunc.append(func)
            onUpdateFuncArgs.append(args)

            return func(args)

        return a

    return func
