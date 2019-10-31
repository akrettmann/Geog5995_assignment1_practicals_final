import random

'''
Instances of the class Agent "share" a 2D list passed as a parameter during 
initialisation, which allows them to determine the size of environment and 
randomize the x and y values within these limits.
'''

class Agent():
    def __init__(self, environment):
        self.environment = environment
        self.store = 0
        #Find out the size of environment inside the agents
        self.width = len(environment);
        self.height = len(environment[0])
        self.x = random.randint(0,self.width)
        self.y = random.randint(0,self.height)
        #self.x = random.randint(0,99)
        #self.y = random.randint(0,99)
            
    def move(self):
        '''
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100
        '''
        if random.random() < 0.5:
            self.x = (self.x + 1) % self.width
        else:
            self.x = (self.x - 1) % self.width
        if random.random() < 0.5:
            self.y = (self.y + 1) % self.height
        else:
            self.y = (self.y - 1) % self.height 
                
    '''
    "Communication" of Agent objects via the environment according to the
    following rules:
    '''
    def eat(self):
        #If more than 10 "eat" ten units, reduce units in envoronment and 
        #store in Agent object
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        
        else:
            #Store what is left
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
        #print(str(self.store))
        if self.store > 100:
            self.environment[self.y][self.x] = self.environment[self.y][self.x] + 100
            #print(str(self))
            self.store = 0
         
         
    def getx(self):
        return self.x
    def setx(self, value):
        self.x = value 
    def gety(self):
        return self.y
    def sety(self, value):
        self.y = value
    
    def __str__(self):
        return "Location x = " + str(self.x) + ", y = " + str(self.y) + ", store = " + str(self.store)