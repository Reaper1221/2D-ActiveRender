# !C:\Users\Hover\Documents\2D-ActiveRender-main\models
from math import *
import json
import numpy as np

MINIMAL = -1000000000000000000000000000000000000000000000000
EPSILON = 2.2

with open('./config.json') as f:
    data = json.load(f)
widht = data['render_config']['withd']
height = data['render_config']['height']

def point(cortej):
    # point model is wonderful

    x, y = cortej[0], cortej[1] 
    points = np.array([[MINIMAL,MINIMAL],[MINIMAL,MINIMAL]])

    points = np.append(points, [[x, y]], axis = 0)

    return points