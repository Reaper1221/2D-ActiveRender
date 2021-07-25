from classes import *
from json import * 

with open('config.json') as f:
    config = load(f)

drawer_ = render.Drawer(config['render_config']['withd'], config['render_config']['height'], config['render_config']['framerate'], config['render_config']['symbol'])
objects_ = objects.Objects()
physics_ = physics.Physics()

withd_ = config['render_config']['withd']
height_ = config['render_config']['height']
