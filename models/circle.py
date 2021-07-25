from math import *
import json
import numpy as np

MINIMAL = -10000000000000000000000000000000000000000000000000
EPSILON = 2.2
with open('./config.json') as f:
    data = json.load(f)
widht = data['render_config']['withd']
height = data['render_config']['height']

def elipse(x, y, r):

    points = np.array([[MINIMAL,MINIMAL],[MINIMAL,MINIMAL]])

    p1, p2 = 1, 1

    for u in range(widht*height): 
        if abs((x-p1)**2 + (y-p2)**2*4 - r**2) < ((r/3)**2):
            points = np.append(points, [[p1, p2]], axis = 0)
    
        p1 = p1 + 1

        if p1 == widht:
            p1 = 1
            p2 = p2 + 1

    return points 