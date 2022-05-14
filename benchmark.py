from classes import render, objects 
from models import elipse, circle, square
import json
import time
import numpy as np

MINIMAL = -100000000000000000000000000000000000000000


with open('config.json') as f:
    config = json.load(f)

o = objects.Objects()
r = render.Drawer(config['render_config']['withd'], config['render_config']['height'], config['render_config']['framerate'], config['render_config']['symbol'])

balls = 0

@o.createObject()
def e(x,y,r):
    return elipse.elipse(x,y,r)

@o.createObject()
def c(x,y,z):
    return circle.circle(x,y,z)

@o.createObject()
def s(x,y,r,t):
    return square.square(x,y,r,t)

info = []
info.append([0,0])
info.append([0,0])
info.append([0,0])
u = 1
i = 12 # Кол-во проходов рендера (ставь 12 и поймёшь что у тебя не комп у мультиварка:) ) изменять тут только это
end = u - 1
ti = time.time()

for j in range(3):
    if j == 0:
        for u in range(u):
            balls = 0
            r.render_calls = 0
            r.render_time = 0
            o.Screen_pointers = np.array([[MINIMAL,MINIMAL],[MINIMAL,MINIMAL], ["END__OBJECT","END__OBJECT"]])
            t = time.time()
            for x in range(i):
                q = time.time() - t
                for y in range(x+1):
                    q = time.time() - t
                    for z in range(y+1):
                        q = time.time() - t
                        e(x,y,z)
                        for w in range(z+1):
                            q = time.time() - t
                            c(x,y,z)
                            for p in range(w+1):
                                s(x,y,z,w)
                                r.render(o)
                                print(f"{x+1} -+- {y+1} -+- {z+1} -+- {w+1} -+- {p+1} ({time.time() - t}) --- {u+1} === {len(o.Screen_pointers)} [{r.render_time}] SINGLE")
                                balls = balls + (r.render_time + r.render_calls) / q 
                            balls = balls + 4 / (r.render_calls + 1) / q
                        balls = balls + 3 / (r.render_time + 1) / q
                    balls = balls + 2 / (r.render_time + 1) / q 
                balls = balls + 1 / time.time() / q

            q = time.time() - t
            info[0][0] = q
            info[0][1] = balls

    if j == 1:
        for u in range(u+1):
            balls = 0
            r.render_calls = 0
            r.render_time = 0
            o.Screen_pointers = np.array([[MINIMAL,MINIMAL],[MINIMAL,MINIMAL], ["END__OBJECT","END__OBJECT"]])
            t = time.time()
            for x in range(i):
                q = time.time() - t
                for y in range(x+1):
                    q = time.time() - t
                    for z in range(y+1):
                        q = time.time() - t
                        e(x,y,z)
                        for w in range(z+1):
                            q = time.time() - t
                            c(x,y,z)
                            for p in range(w+1):
                                s(x,y,z,w)
                                r.duoRender(o)
                                print(f"{x+1} -+- {y+1} -+- {z+1} -+- {w+1} -+- {p+1} ({time.time() - t}) --- {u+1} === {len(o.Screen_pointers)} [{r.render_time}] DUO")
                                balls = balls + (r.render_time + r.render_calls) / q 
                            balls = balls + 4 / (r.render_calls + 1) / q
                        balls = balls + 3 / (r.render_time + 1) / q
                    balls = balls + 2 / (r.render_time + 1) / q 
                balls = balls + 1 / time.time() / q

            q = time.time() - t
            info[1][0] = q
            info[1][1] = balls

    if j == 2:
        for u in range(u+1):
            balls = 0
            r.render_calls = 0
            r.render_time = 0
            o.Screen_pointers = np.array([[MINIMAL,MINIMAL],[MINIMAL,MINIMAL], ["END__OBJECT","END__OBJECT"]])
            t = time.time()
            for x in range(i):
                q = time.time() - t
                for y in range(x+1):
                    q = time.time() - t
                    for z in range(y+1):
                        q = time.time() - t
                        e(x,y,z)
                        for w in range(z+1):
                            q = time.time() - t
                            c(x,y,z)
                            for p in range(w+1):
                                s(x,y,z,w)
                                r.QuadRender(o)
                                print(f"{x+1} -+- {y+1} -+- {z+1} -+- {w+1} -+- {p+1} ({time.time() - t}) --- {u+1} === {len(o.Screen_pointers)} [{r.render_time}] QUAD")
                                balls = balls + (r.render_time + r.render_calls) / q 
                            balls = balls + 4 / (r.render_calls + 1) / q
                        balls = balls + 3 / (r.render_time + 1) / q
                    balls = balls + 2 / (r.render_time + 1) / q 
                balls = balls + 1 / time.time() / q

            q = time.time() - t
            info[2][0] = q
            info[2][1] = balls
            
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print(f"\nthe average value for {u+1} tests of {i} runs each\n")
print(f"\nthere were {u+1} tests in single mode and {u+1} tests in double mode and {u+1} tests in quad mode\n")
print("\n\nSINGLE RENDER\n")
print(f"\nYOUR RESULT {info[0][1]} BALLS\nTEST TIMES {info[0][0]} SECONDS")
print("\n\nDUAL THREAD RENDER")
print(f"\nYOUR RESULT {info[1][1]} BALLS\nTESTS TIME {info[1][0]} SECONDS")
print("\n\nQUAD THREAD RENDER")
print(f"\nYOUR RESULT {info[2][1]} BALLS\nTESTS TIME {info[2][0]} SECONDS")
print("\nMORE INFO\n")
print(f"render calls = {r.render_calls}\npoints = {len(o.Screen_pointers)}\nbenchmark time = {time.time() - ti}\nall render calls = {r.render_calls * 3}\nren dering time of the last frame = {r.render_time}")


"""

"""

"""

"""