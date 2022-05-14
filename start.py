from scripts import *
from environment import *
from classes import *
from functions import *
import time


# Запускаем функции старта (Если они есть)
args_point = 0
if len(onStartDecorator.onStartFunc) != 0: 
    for func in onStartDecorator.onStartFunc:
        func(onStartDecorator.onStartFuncArgs[args_point])
        args_point = args_point + 1

while True:

    try:
        # time.sleep(1/drawer_.FPS)
        # Запускаем функции (Если они есть)
        args_point = 0
        if len(onUpdateDecorator.onUpdateFunc) != 0: 
            for func in onUpdateDecorator.onUpdateFunc:
                func(onUpdateDecorator.onUpdateFuncArgs[args_point])
                args_point = args_point + 1

        drawer_.QuadRender(objects_)

        print(0/0)

    except KeyboardInterrupt:
        # print(f"")
        exit()