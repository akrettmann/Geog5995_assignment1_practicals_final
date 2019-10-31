import random

class Agent():
        '''
        Initialise coordinates with random intergers on creation
        '''
        def __init__(self):
            self._x = random.randint(0,99)
            self._y = random.randint(0,99)
        '''
        Move agent by randomly stepping up or down each coordinate separately.
        The modulus operator is used to ensure that the coordinates are between
        0 and 99
        '''
        def move(self):
            if random.random() < 0.5:
                self._x = (self._x + 1) % 100
            else:
                self._x = (self._x - 1) % 100
            if random.random() < 0.5:
                self._y = (self._y + 1) % 100
            else:
                self._y = (self._y - 1) % 100
            
             
        def getx(self):
            return self._x
        def setx(self, value):
            self._x = value 
        def gety(self):
            return self._y
        def sety(self, value):
            self._y = value
        
