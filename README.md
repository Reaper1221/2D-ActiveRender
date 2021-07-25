Русская версия:

И так, приветствую тебя в замечательно движке ActiveRender!
Тут ты прочитаешь подробные инструкции по созданию анимации любой сложности 

1.0 Инструкция к началу
И так, ты распаковал архив с файлами движка
Давай создадим проект!
Для этого открой терминал/консоль/cmd и перейди в деректорию с ActiveRender
Дальше выполни следующию команду:

>>> python app.py

Если дальше введи имя проекта, разрешение консоли, задержку отображения, символ пикселя
Вводи всё в том порядке, в котором просит программа
Разрешение консоли можно взять таким образом -> 

открой консоль -> кликни по её ферхней части правой кнопкой мыши -> выбери свойства -> 
-> в появивщемся окне выбери "расположения" -> теперь смотри на пункт размер окна, там отобразиться ширина и высота которую ты должен будешь ввести!

2.0
И так, ты создал проект
Теперь чтобы создать (класс/функцию/модель/скрипт) тебе надо снова открыть терминал/консоль/cmd
и перейти в деректорию с ActiveRender
там снова запусти комманду

>>> python app.py

и выберай что тебе нужно
Движок сам всё сделает за тебя

3.0
Список декораторов

@onUpdate - функция вызывается в начале цикла (не вовремя отрисовки)
(Храниться в functions.onUpdateDecorator)

@onStart - функция вызываестя единолично и только при старте рендеринга
(Храниться в functions.onStartDecorator)

@onRender - функция вызывается при начале отрисовки
(Храниться в экземляре класса (render), в файле environment.py)

@createObject - функция создания объекта (должна возвращать что то подобное этому [[0,0],[0,1]],
то есть координаты точек в формате массива numpy)

Список будет пополнять!

4.0
Список классов

Drawer - Главный класс отрисовки

Objects - Класс хранит все точки для рендеринга, так же может их перемещать
имеет следующие методы - {
    move() - служит для перемещения объекта
}

5.0
И так когды вы уже сделали свою анимацию/рендер давай те взглянем на него!
снова открываем терминал/консоль/cmd и переходим в деректорию с ActiveRender там запускай комманду

>>> python start.py

наслаждайся!


English version:

And so, I welcome you to the wonderful ActiveRender engine!
Here you will read detailed instructions for creating animations of any complexity

1.0 Instructions to start
And so, you unpacked the archive with the engine files
Let's create a project!
To do this, open the terminal / console/cmd and go to the directory with ActiveRender
Then run the following command:

>>> python app.py

If you continue, enter the project name, console resolution, display delay, pixel symbol
Enter everything in the order in which the program asks
The console resolution can be taken in this way - >

open the console -> right - click on its upper part -> select properties ->
-> in the window that appears, select "locations" -> now look at the window size item, the width and height that you will have to enter will be displayed there!

2.0
And so, you have created a project
Now to create (a class/function/model/script) , you need to open the terminal/console/cmd again
and go to the directory with ActiveRender, run the command
there again

>>> python app.py

and choose what you need
The engine will do everything for you by itself

3.0
List of decorators

@onUpdate-the function is called at the beginning of the loop (not at the time of rendering)
(Stored in functions.onUpdateDecorator)

@OnStart-the function is called alone and only at the start of rendering
(Stored in functions.onStartDecorator)

@OnRender-the function is called at the beginning of rendering
(Stored in the instance of the class (render), in the file environment.py)

@CreateObject-object creation function (should return something like this [[0,0], [0,1]],
that is, the coordinates of the points in the numpy array format)

The list will be replenished!

4.0
List of classes

Drawer - The main drawing class

Objects-The class stores all the points for rendering, it can also move them
has the following methods - {
move () - serves to move the object
}

5.0
And so when you have already done your animation/render, let's take a look at it!
open the terminal / console/cmd again and go to the directory with ActiveRender there run the command

>>> python start.py

enjoy it!