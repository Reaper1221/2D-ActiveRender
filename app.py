import os
import json

def start_project():
    fps = int(input("please enter the maximum fps: "))
    withd = int(input("please enter the width: "))
    height = int(input("please enter the height: "))
    project_name = input("please enter the project name: ")
    render_symbol = input("please enter the pixel symbol: ")

    with open('config.json') as f:
        data = json.load(f)

    data["render_config"]['withd'] = withd
    data["render_config"]['height'] = height
    data["render_config"]['framerate'] = fps
    data["render_config"]['symbol'] = render_symbol

    data["project_config"]['name'] = project_name
    data["project_config"]['start?'] = 1

    with open('config.json', 'w') as f:
        json.dump(data, f, sort_keys=True, indent=4)

def Create():
    print("Class [1]")
    print("Model [2]")
    print("Function [3]")
    print("Script [4]")
    a = int(input("What do you want to create: "))
    name = input("Ok, what is the name of this without .py: ")

    if a == 1:
        os.chdir("classes")
        obj = open(f"{name}.py", "w")
        obj.write(f"# !{os.getcwd()}\nimport numpy as np\n\nclass {name}:\n\n    def __init__(self):\n\n        print(\"Hello World!\") \n\n    def class_name(self):\n\n        return self.__class__.__name__")
        obj.close()
        obj = open("__init__.py", "a+")
        obj.write(f"\n# !{os.getcwd()}\{name} - directory of this file\nfrom . import {name}")
        obj.close()
        os.chdir("..")
        obj = open("environment.py", "a+")
        obj.write(f"{name}_ = {name}.{name}()")

    elif a == 2:
        os.chdir("models")
        obj = open(f"{name}.py", "w")
        obj.write(f"# !{os.getcwd()}\nfrom math import *\nimport json\nimport numpy as np\n\nMINIMAL = -1000000000000000000000000000000000000000000000000\nEPSILON = 2.2\n\nwith open('./config.json') as f:\n    data = json.load(f)\nwidht = data['render_config']['withd']\nheight = data['render_config']['height']\n\ndef {name}(x, y):\n    # {name} model is wonderful\n\n    points = np.array([[MINIMAL,MINIMAL],[MINIMAL,MINIMAL]])\n\n    return points")
        obj.close()
        obj = open("__init__.py", "a+")
        obj.write(f"\n# !{os.getcwd()}\{name} - directory of this file\nfrom . import {name}")
        obj.close()

    elif a == 3:
        os.chdir("functions")
        obj = open(f"{name}.py", "w")
        obj.write(f"# !{os.getcwd()}\nimport numpy as np\n\ndef {name}(args: list):\n\n    return args")
        obj.close()
        obj = open("__init__.py", "a+")
        obj.write(f"\n# !{os.getcwd()}\{name} - directory of this file\nfrom . import {name}")
        obj.close()

    elif a == 4: 
        os.chdir("scripts")
        obj = open(f"{name}.py", "w")
        obj.write(f"# !{os.getcwd()}\nfrom environment import objects_\nfrom functions import onStartDecorator\nfrom functions import onUpdateDecorator\nfrom models import *\n\n@objects_.createObject(True)\ndef elipse_func(x,y,r):\n    return elipse.elipse(x,y,r)\n\n@onStartDecorator.onStart(\"hello World!\")\ndef start(text):\n    elipse_func(60,20,10)\n    print(text)\n    update()\n\n@onUpdateDecorator.onUpdate(True)\ndef update(isTrue):\n    if isTrue:\n        print(\"Hello World!\")\n\nstart()\n")
        obj.close()
        obj = open("__init__.py", "a+")
        obj.write(f"\n# !{os.getcwd()}\{name} - directory of this file\nfrom . import {name}")
        obj.close()

    print("succesfuly!")

def Change():
    input_int = int(input("What do you want change?\n[1]physics\n[2]light\n[3]project name\n>>>"))
    with open('config.json') as f:
        data = json.load(f)

    if input_int == 1:
        data['physics_config']['acceleration of free fall'] = float(input("please enter the acceleration of free fall: "))
        data['physics_config']['pixel mass'] = float(input("please enter the pixel mass: "))
        data['physics_config']['power in one point'] = float(input("please enter the power in one point: "))
        data['physics_config']['inertia multiplier'] = float(input("please enter the inertia multiplier: "))
    
    elif input_int == 2: 
        data['light_config']['light_power'] = float(input("please enter the light_power: "))

    elif input_int == 3: 
        data['project_config']['project_name'] = input('Please enter the new project name: ')

    with open('config.json', 'w') as f:
        json.dump(data, f, sort_keys=True, indent=4)

if __name__ == "__main__":

    # Проверка на старт проекта
    with open('config.json') as f:
        data = json.load(f)

    if data["project_config"]['start?'] == 0:
        start_project()

    input_int = int(input("What do you want?\n[1]change the configuration\n[2]create a new file\n>>>"))
    if input_int == 2: Create()
    elif input_int == 1: Change()


# планы
"""
1. Добавить новых фигур
2. Добавить новых декораторов
3. Оптимизировать всё по максимому 
4. Добавить настройки редеринга +
5. Глобальное окружение + 
6. Освещение
7. Физика
8. Полная оптимизация всего и вся
9. Убрать артефакты которые происходят при движении объекта +
10. Перевести все коментарии на английский язык
11. Реализовать демонстрацию {
    Всё рендериться на одном компьютере после чего уже передаётся готовая картинка другому пользователю
    }
12. Упростить програмирование...    
"""