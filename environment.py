from tokenize import ContStr
from numpy import squeeze
from classes import *
from classes.prefabs import Prefab
from classes.vectors import Vec2, Vec3, Vec4
from models import *
from json import * 
from random import *

with open('config.json') as f:
    config = load(f)

shag = 0

drawer_ = render.Drawer(config['render_config']['withd'], config['render_config']['height'], config['render_config']['framerate'], config['render_config']['symbol'])
engine_ = engine.Engine(config['engine_config'], config['render_config']['withd'], config['render_config']['height'])
objects_ = objects.Objects(engine_)
debug_ = debug.Debug(config['debug_config']['mode'])


withd_ = config['render_config']['withd']
height_ = config['render_config']['height']


# Preafabs

h = Prefab((0,29,58), line.line)

test = Prefab((10,10,7), circle.circle)
test._init_()

# Vectors