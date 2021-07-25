import numpy as np
import json

class Physics:
    
    def __init__(self) -> None:
        
        with open('./config.json') as f:
            data = json.load(f)
        
        self.acceleration = data['physics_config']['acceleration of free fall']
        self.inertia = data['physics_config']['inertia multiplier']
        self.mass = data['physics_config']['pixel mass']
        self.power = data['physics_config']['power in one point']

    def get_mass(self, objects_):
        return len(objects_.Screen_pointers) * self.mass

    @property
    def inertia(self):
        return self.inertia

    @property
    def acceleration(self):
        return self.acceleration
    
    @property
    def mass(self):
        return self.mass
    
    @property
    def power(self):
        return self.power
