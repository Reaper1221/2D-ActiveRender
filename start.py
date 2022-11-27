from environment import *
from functions.shag_animate import shag_inc
from scripts import *
from environment import *
from classes import *
from functions import *
import time
import sys
import pygame as pg
from math import *

shag_animate.shag_to_null()     

info_real = ["FPS","render-time","points-count","system-time","anim-time", "points-memory", "last-optimize-time", "optimize-circle", "programm-memory-size"]
info_anim = ["FPS","render-time","points-count","system-time","anim-time", "points-memory", "last-optimize-time", "optimize-circle", "programm-memory-size","cadr-render","progress"]

t_t_t = time.time()

def real(t_t, t_t_t):
    debug_.debug_window_part(info_real, [
                    int(1/(drawer_.render_time+0.00001)),
                    round(drawer_.render_time, 5),
                    len(objects_.Screen_pointers),
                    round(time.time() - t_t, 5),
                    round(time.time() - t_t_t,5),
                    f"{round(sys.getsizeof(objects_.Screen_pointers)/1024/1024, 5)} MB",
                    engine_.optimize_time,
                    f"{engine_.optimize_circle} of {engine_.max_optimize_circle}",
                    f"{engine_.process_memory_MB()} MB"
                ])

def anim(t_t, t_t_t, shag, cadrs):
    debug_.debug_window_part(info_anim, [
                    int(1/(drawer_.render_time)),
                    round(drawer_.render_time, 5),
                    len(objects_.Screen_pointers),
                    round(time.time() - t_t, 5),
                    round(time.time() - t_t_t,5),
                    f"{round(sys.getsizeof(objects_.Screen_pointers)/1024/1024, 5)} MB",
                    engine_.optimize_time,
                    f"{engine_.optimize_circle} of {engine_.max_optimize_circle}",
                    f"{engine_.process_memory_MB()} MB",
                    shag,
                    f"{round(shag/(int(cadrs)/100), 3)}%"
                ])
def start(cadrs, stopmode):
    shag = 0
    cadrs = int(cadrs)
    if cadrs == 0: animmode = 0
    else: animmode = 1
    cadrs = abs(int(cadrs) + 1)
    if animmode == 0:
        while True:
            try:
                t_t = time.time()
                if shag == 1: 
                    args_point = 0
                    if len(onStartDecorator.onStartFunc) != 0: 
                        for func in onStartDecorator.onStartFunc:
                            func(onStartDecorator.onStartFuncArgs[args_point])
                            args_point = args_point + 1
                # Запускаем функции (Если они есть)
                args_point = 0
                if len(onUpdateDecorator.onUpdateFunc) != 0: 
                    for func in onUpdateDecorator.onUpdateFunc:
                        func(onUpdateDecorator.onUpdateFuncArgs[args_point])
                        args_point = args_point + 1

                drawer_.duoRender(objects_)
                objects_._set_points(engine_.start_optimaze(objects_))
                real(t_t, t_t_t)
                
                shag_inc()
                shag = shag + 1
                if stopmode == 1: input()

            except KeyboardInterrupt:
                # print(f"")
                exit()
    else: 
        while True:
            try:
                t_t = time.time()
                if shag == 1: 
                    args_point = 0
                    if len(onStartDecorator.onStartFunc) != 0: 
                        for func in onStartDecorator.onStartFunc:
                            func(onStartDecorator.onStartFuncArgs[args_point])
                            args_point = args_point + 1
                # Запускаем функции (Если они есть)
                args_point = 0
                if len(onUpdateDecorator.onUpdateFunc) != 0: 
                    for func in onUpdateDecorator.onUpdateFunc:
                        func(onUpdateDecorator.onUpdateFuncArgs[args_point])
                        args_point = args_point + 1

                drawer_.animate(objects_)
                objects_._set_points(engine_.start_optimaze(objects_))
                anim(t_t, t_t_t, shag, cadrs)
                
                shag_inc()
                if shag == cadrs:
                    input("Press enter, for compete")
                    drawer_.anim_start()
                    pg.quit()
                    exit()
                shag = shag + 1
                

            except KeyboardInterrupt:
                input("Press enter, for compete")
                drawer_.anim_start()
                pg.quit()
                exit()

debug_._init_start_method_(start)

if __name__ == "__main__":
    debug_.window.mainloop()