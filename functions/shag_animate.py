import numpy as np
import json

# Добавление кадра
def shag_inc():
    with open('__shag_animation.json') as f:
        data = json.load(f)
    
    shag = data['shag']
    shag = shag + 1
    data['shag'] = shag

    with open('__shag_animation.json', 'w') as f:
        json.dump(data, f, sort_keys=True, indent=4)

def shag_to_null():
    with open('__shag_animation.json' , 'r') as f:
        data = json.load(f)

    data['shag'] = 0.0

    with open('__shag_animation.json', 'w') as f:
        json.dump(data, f, sort_keys=True, indent=4)

# Получение текущего шага\кадра
def get_shag():
    with open('__shag_animation.json') as f:
        data = json.load(f)
    
    return data['shag']
