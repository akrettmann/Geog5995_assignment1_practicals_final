
import random

'''
Instances of the class Agent "share" a 2D list passed as a parameter
during initialisation, which allows them to determine the size of
environment and randomize the x and y values within these limits.

Furthermore, the list of all agents is passed as an argument which allows
a direct "communication" among the agents. The method <share-with-neighbours>
accesses, i.e. reads and writes, the store of the other agents in the near
neighbourhood. What is considered to be "near" is defined through the argument
<neighbourhood>.
'''

class Agent():
    def __init__(self, environment, agents_list, random_seed):
        self.environment = environment
        self.agentslist=agents_list
        self.store = 0
        '''
        Find out the size of environment in which the agents operate
        and initialise agents such that their coordinates stay within
        the limits of the environment. For randomising the coordinates
        an initial "seed" value is provided as an argument to the method
        '''
        self.width = len(environment);
        self.height = len(environment[0])
        random.seed(random_seed)
        self._x = random.randint(0,self.width)
        self._y = random.randint(0,self.height)
        #self.x = random.randint(0,99)
        #self.y = random.randint(0,99)

    def move(self):

        '''
        Making sure that agents coordinates stay within environment limits
        by using the modulus operator.
        '''
        if random.random() < 0.5:
            self._x = (self._x + 1) % self.width
        else:
            self._x = (self._x - 1) % self.width
        if random.random() < 0.5:
            self._y = (self._y + 1) % self.height
        else:
            self._y = (self._y - 1) % self.height

    '''
    "Communication" of Agent objects via the environment and the other agents
    according to the following rules:
    '''

    def eat(self):
        '''
        If more than ten units in agents location, "eat" 10 units in envoronment,
        i.e. store 10, and leave the rest in that location of environment. Otherwise
        "eat" all whats left in that spot. If total amount "eaten" amounts more than
        100, "sick up" all 100 units into environment.
        '''

        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10

        else:
            # Store what is left
            self.store += self.environment[self._y][self._x]
            self.environment[self._y][self._x] = 0
        #print(str(self.store))
        if self.store > 100:
            self.environment[self._y][self._x] = self.environment[self._y][self._x] + 100
            #print(str(self))
            self.store = 0




    def share (self, neighbourhood):
        '''
        Share with near neighbours defined by the argument <neighbourhood>
        by summing up the two stores and sharing equally, i.e. the method assigns
        the average of the two stores to each of the two stores.
        '''
        for otheragent in self.agentslist:
            if(self != otheragent):
                if self.distance_to_otheragents (otheragent) <= neighbourhood:
                    equalshare = (self.store + otheragent.store) / 2
                    self.store = equalshare
                    otheragent.store = equalshare

    def distance_to_otheragents (self, otheragent):
        return (((self.x - otheragent.x)**2 + (self.y - otheragent.y)**2)**0.5)

    @property
    def x(self):
        return self._x
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value

    @property
    def y(self):
        return self._y
    def gety(self):
        return self._y
    def sety(self, value):
        self._y = value

    def __str__(self):
        return "Location x = " + str(self._x) + ", y = " + str(self._y) + ", store = " + str(self.store)
