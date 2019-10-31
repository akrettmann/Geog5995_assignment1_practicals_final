import random
import operator
import matplotlib.pyplot


#Create container (list structure) to store agent coordinates.
#and initalise with random integers between 0 and 99.
#Add coordinate to first and second agent
agents = []
agents.append([random.randint(0,99),random.randint(0,99)])
agents.append([random.randint(0,99),random.randint(0,99)])


print("Create and initialise agents list")

print("X-coordinate of agent 1: ", agents[0][1])
print("Y-coordinate of agent 1: ", agents[0][0])
print("X-coordinate of agent 2: ", agents[1][1])
print("Y-coordinate of agent 2: ", agents[1][0])

'''
y0 = random.randint(0,99)
x0 = random.randint(0,99)
agents.append([y0,x0])
'''
print ("inital locations" , agents)

#Calculate distance between the two agents using Pythagoras' theorem
print("Calculate distance between the two agents using Pythagoras' theorem")

distance= ((agents[0][0] - agents[1][0]) ** 2 + (agents[0][1] -agents[1][1]) **2 ) **0.5

print ("Distance between agents", distance)

#Calculate furtherst east agent, i.e. agent with largest x-coordinate
print ("Agent with largest x-coordinate", max(agents, key=operator.itemgetter(1)))


matplotlib.pyplot.ylim(0,99)
matplotlib.pyplot.xlim(0,99)

'''
This version does not need the function max
if agents[0][1] < agents[1][1] :
    matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
    matplotlib.pyplot.scatter(agents[1][1],agents[1][0],color='red')
else:
    matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
    matplotlib.pyplot.scatter(agents[0][1],agents[0][0],color='red')
'''

matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
matplotlib.pyplot.scatter(max(agents, key=operator.itemgetter(1))[1],max(agents, key=operator.itemgetter(1))[0],color='red')

#matplotlib.pyplot.scatter(m[1],m[0],color='red')
matplotlib.pyplot.show()

