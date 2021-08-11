

class Prefab:

    def __init__(self,args:list, model_func):
        self.__args = args
        self.__model = model_func

    def init(self):
        self.__points = self.__model(self.__args)

    def get(self):
        return self.__points