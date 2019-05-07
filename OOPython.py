import numpy as np
import time
ID = list()
def DNA(ID):
    speed = np.random.rand()
    size = np.random.rand()
    sense_radius = np.random.rand()
    ID.append(len(ID))
    return speed, size, sense_radius

class maps:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.size = width*height

class creature:
    def __init__(self,IDd,region):
        self.speed, self.size, self.sense_radius = DNA(IDd)
        self.ID = IDd
        self.energy = 100
        self.region = region
        self.x = np.random.randint(self.region.width,size=1)[0]
        self.y = np.random.randint(self.region.height,size=1)[0]
    def move(self):
        if np.random.randint(2,size=1)[0] > 0:
            charge_x = -1
        else:
            charge_x = 1
        if self.x < self.region.width:
            if self.x > 0:
                self.x += np.random.randint(2,size=1)[0]*charge_x
            else:
                self.x += np.random.randint(2,size=1)[0]
        else:
            self.x += np.random.randint(2,size=1)[0]*-1
        if np.random.randint(2,size=1)[0] > 0:
            charge_y = -1
        else:
            charge_y = 1
        if self.y < self.region.height:
            if self.y > 0:
                self.y += np.random.randint(2,size=1)[0]*charge_y
            else:
                self.y += np.random.randint(2,size=1)[0]
        else:
            self.y += np.random.randint(2,size=1)[0]*-1
        
mapa = maps(500,500)
mapa.width
blob = creature(ID,mapa)
def move_your_blob(steps):
    start_time = time.time()
    
    elapsed_time = time.time() - start_time
    print("Time to Run: " + str(elapsed_time))
move_your_blob(5000000)
