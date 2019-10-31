import random as rd

'''
Instances of the class Agent "share" a 2D list passed as a parameter
during initialisation, which allows them to determine the size of
environment and randomize the x and y values within these limits.

Furthermore, the list of all agents is passed as an argument which allows
a direct "communication" among the agents. The method <share-with-neighbours>
accesses, i.e. reads and writes, the store of the other agents in the near 
neighbourhood. What is considered to be "near" is defined through the argument
<neighbourhood>.

Random_seed -- a number used to initialise the random seed for this agent.

The coordinates y_value and x_value comming from the provided web data
are passed as an argument.
'''


class Agent():
    def __init__(self, model_environment, agents_list, random_seed, y_value, x_value):
        '''
        Initialise agents such that their coordinates stay within
        the limits of the environment.
        '''
        if (random_seed == None):
            rd.seed(0) # defaul random seed to 0
        else:
            rd.seed(random_seed)
        if y_value == None:
            self.y=rd.randint(0, len(model_environment))
        else :
            self.y=y_value
        if x_value == None:
            self.x=rd.randint(0, len(model_environment))
        else :
            self.x=x_value
        self.environment=model_environment
        self.store=0
        self.otheragents=agents_list
        self.count_neighbours=0

    def move(self):
        '''
        Making sure that agents coordinates stay within environment limits
        by using the modulus operator. 
        '''
        if rd.random()<0.5:
            self.y=(self.y+1) % len(self.environment)
        else:
            self.y=(self.y-1) % len(self.environment)
        if rd.random()<0.5:
            self.x=(self.x+1) % len(self.environment)
        else:
            self.x=(self.x-1) % len(self.environment)
      
        
    def eat(self):
        ''' 
        If more than ten units in agents location, "eat" 10 units in envoronment,
        i.e. store 10, and leave the rest in that location of environment. Otherwise
        "eat" all whats left in that spot. If total amount "eaten" amounts more than
        100, "sick up" all 100 units into environment.
        '''
        
        if self.environment[self.y][self.x] > 10:
                self.environment[self.y][self.x] -= 10
                self.store += 10
            
        else:
                # Store what is left
                self.store += self.environment[self.y][self.x]
                self.environment[self.y][self.x] = 0
            #print(str(self.store))
        if self.store > 100:
                self.environment[self.y][self.x] = self.environment[self.y][self.x] + 100
                #print(str(self))
                self.store = 0
    
    
    def distance(self, secondagent):
        return (((self.x - secondagent.x)**2) + ((self.y - secondagent.y)**2))**0.5
        
              
        
    def share(self, distance_of_neighbourhood):
        '''
        Share with near neighbours defined by the argument <neighbourhood> 
        by summing up the two stores and sharing equally, i.e. the method assigns
        the average of the two stores to each of the two stores. 
        '''
        for i in self.otheragents:
            if self.distance(i) < distance_of_neighbourhood:
                average=(self.store+i.store)/2
                self.store=average
                i.store=average 
                self.count_neighbours=self.count_neighbours+1

