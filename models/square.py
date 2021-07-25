from math import *
import json
import numpy as np

MINIMAL = -10000000000000000000000000000000000000000000000000
EPSILON = 2.2
with open('./config.json') as f:
    data = json.load(f)
widht = data['render_config']['withd']
height = data['render_config']['height']

def square(x, y, scalex, scaley):

    points = np.array([[MINIMAL,MINIMAL],[MINIMAL,MINIMAL]])

    points = np.append(points,[[x - scalex, y - scaley]], axis = 0)
    points = np.append(points,[[x + scalex, y - scaley]], axis = 0) 
    points = np.append(points,[[x - scalex, y + scaley]], axis = 0)
    points = np.append(points,[[x + scalex, y + scaley]], axis = 0) 

    for r in range(abs(scalex * 2 )): points = np.append(points,[[x - scalex + r, y - scaley]], axis = 0)
    for r in range(abs(scaley * 2 )): points = np.append(points,[[x - scalex, y - scaley + r]], axis = 0)
    for r in range(abs(scalex * 2 )): points = np.append(points,[[x + scalex - r, y + scaley]], axis = 0)
    for r in range(abs(scaley * 2 )): points = np.append(points,[[x + scalex, y + scaley - r]], axis = 0)

    return points