from numpy import *
from sys import getsizeof

class Prefab():

    def __init__(self, args, model_func) -> None:
        self.__args = args
        self.__model = model_func       

    def _init_(self) -> None:
        self.__points = self.__model(self.__args)

    def edit_args(self, args) -> None:
        self.__args = args
    
    def edit_model(self, model_func) -> None:
        self.__model = model_func

    def get(self) -> None:
        return self.__points

    def get_args(self) -> None:
        return self.__args
    
    def get_model(self) -> None:
        return self.__model
    
    def del_points(self) -> None:
        del self.__points
        self.__points = []

    def get_memory(self) -> float: 
        return getsizeof(self.__points) + getsizeof(self.__model) + getsizeof(self.__args)
