from pickletools import optimize
from . import objects
import numpy as np
import os
import sys
import psutil
import time

class Engine:

    def __init__(self, json_config, w, h) -> None:
        self._version_ = '1.6'

        self.max_points = json_config['max-points']
        self.max_points_size_mb = json_config['max-points-size-mb']
        self.programm_size_mb = json_config['max-programm-size']
        self.max_optimize_circle = json_config['max-optimize-circle']
        self.minimal_point = json_config['minimal-point']
        self.optimaze_memory = json_config['optimize-memory']
        self.movement = json_config["movment-points"]
        self.delete_points = json_config["del-points"]

        self.optimize_circle = 0

        self.optimize_time = 0

        self.max_w = w + 1
        self.max_h = h + 1

    def init(self) -> None:
        pass

    def _get_version_(self) -> str: return self._version_

    def start_optimaze(self, objs: objects) -> None:
        t = time.time()

        points = objs.Screen_pointers
        if self.optimize_circle < self.max_optimize_circle and self.optimaze_memory:
            if len(points) >= self.max_points:
                self.optimize_circle = self.optimize_circle + 1 
                self.optimize_time = round(time.time() - t, 5)
                return self.__optimize(points)
            elif sys.getsizeof(points)/1024/1024 >= self.max_points_size_mb:
                self.optimize_circle = self.optimize_circle + 1 
                self.optimize_time = round(time.time() - t, 7)
                return self.__optimize(points)
            elif Engine.process_memory_MB() >= self.programm_size_mb :
                self.optimize_circle = self.optimize_circle + 1 
                self.optimize_time = round(time.time() - t, 7)
                return self.__optimize(points)
            else: 
                return points
        else:
            return points
            

    def __optimize(self, points) -> None:
        del_array_id = []
        for x in range(len(points)):
            if type(points[x, 0]) != type(str()): 
                if points[x, 0] <= self.minimal_point or points[x, 1] <= self.minimal_point:
                    del_array_id.append(x)
                if points[x, 0] >= self.max_w or points[x, 1] >= self.max_h:
                    del_array_id.append(x)

        del_array_id = list(set(del_array_id))
        del_array_id.sort()
        del_array_id.reverse()

        for x in del_array_id: 
            points = np.delete(points, x, axis=0)

        if not self.movement and not self.delete_points:
            points = np.unique(points, axis=0)

        return points

    def get_movevment(self) -> bool: return self.movement

    def get_delete(self) -> bool: return self.delete_points

    @staticmethod
    def process_memory_MB() -> float: 
        process = psutil.Process(os.getpid())
        mem_info = process.memory_info()
        return mem_info.rss/1024/1024
    
    @staticmethod
    def process_memory_KB() -> float: 
        process = psutil.Process(os.getpid())
        mem_info = process.memory_info()
        return mem_info.rss/1024

    @staticmethod
    def process_memory_B() -> float: 
        process = psutil.Process(os.getpid())
        mem_info = process.memory_info()
        return mem_info.rss

if __name__ == "__main__":
    enigne = Engine()
    print(f" version: {enigne._get_version_() }")