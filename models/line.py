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

def line(cortej):
    # line model is wonderful

    k, posy, posx = cortej[0], cortej[1], cortej[2]
    points = np.array([[MINIMAL,MINIMAL],[MINIMAL,MINIMAL]])

    p1, p2 = 1, 1

    if k == 0: k = 0.00001

    cof = k**3
    b = cof
    cof = k
    k = b
    del b

    if k > 1.5:
        b = cof
        cof = k
        k = b
        cof = k/1.6
        del b

    if k > 2.5: cof = 1.2 

    for u in range(widht*height): 
        x = posx - p1
        y = posy - p2
        if k*x-y > abs(k/cof/2):
            if k*x-y < abs(k*cof*2):
                points = np.append(points, [[p1, p2]], axis = 0)
    
        p1 = p1 + 1

        if p1 == widht:
            p1 = 1
            p2 = p2 + 1
    return points