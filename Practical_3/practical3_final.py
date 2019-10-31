import random
import operator
import matplotlib.pyplot

agents = []
number_of_agents = 10
number_of_iterations = 100

print("Number of agents: ", number_of_agents)
print("Number of moves: ", number_of_iterations)

'''
Initialise all agents with random integers
'''
print("Initialise all agents with random integers")
for i in range (number_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])
    
print ("Inital locations")
print (agents)

'''
Move each agent <number_of_iterations> times.
''' 
print("Moving agents")
for j in range (number_of_iterations):    
    for i in range (0,number_of_agents):
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] =(agents[i][1] - 1) % 100
            
    #print ("moved agents", agents, "at iteration: ", j)

#distance= ((agents[0][0] - agents[1][0]) ** 2 + (agents[0][1] -agents[1][1]) **2 ) **0.5
print ("Locations after",number_of_iterations, " iterations: ")
print (agents)
#print ("Distance between agents", distance)

#print ("Agent with largest x-coordinate", max(agents, key=operator.itemgetter(1)))

'''
Plotting agents
'''
print("Plotting agents")
matplotlib.pyplot.ylim(0,99)
matplotlib.pyplot.xlim(0,99)
for i in range (number_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
        
#m =max(agents, key=operator.itemgetter(1))
#matplotlib.pyplot.scatter(max(agents, key=operator.itemgetter(1))[1],max(agents, key=operator.itemgetter(1))[0],color='red')
#if agents[0][1] < agents[1][1] :
#    matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
#else:
#    matplotlib.pyplot.scatter(agents[1][1],agents[1][0])

#matplotlib.pyplot.scatter(m[1],m[0],color='red')
matplotlib.pyplot.show()

