# !C:\Users\Hover\Documents\2D-ActiveRender-main\scripts
from time import *
from environment import objects_
from functions import onStartDecorator
from functions import onUpdateDecorator
from models import *

t = time()

@objects_.createObject(True)
def elipse_func(x,y,r):
    return elipse.elipse(x,y,r)

@onStartDecorator.onStart("hello World!")
def start(text):
    elipse_func(60,20,10)
    print(text)
    update()

@onUpdateDecorator.onUpdate(True)
def update(isTrue):
    
    if isTrue:
        print(time() - t)

start()
