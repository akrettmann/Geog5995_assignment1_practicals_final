#import operator
import matplotlib.pyplot
#import random
import agentframework5 as af

number_of_moves = 100
number_of_agents = 10
agentslist = []
distances = []

def distance_between (agents_row_a, agents_row_b):
        return (((agents_row_a._x - agents_row_b._x)**2 + (agents_row_a._y - agents_row_b._y)**2)**0.5)

print("Number of agents", number_of_agents)
    
'''
Generate <number_of_agents> instances of class <Agent>
'''
for i in range(number_of_agents):
    agentslist.append(af.Agent())
#print("Type of Agent",type(agentlist[0])
   
'''
Moving Agents <number_of_moves> times
'''

for j in range (number_of_moves):  
    for i in range (0,number_of_agents):
        agentslist[i].move()
            
'''
Plotting agents
'''
matplotlib.pyplot.ylim(0,99)
matplotlib.pyplot.xlim(0,99)
for i in range (number_of_agents):
    matplotlib.pyplot.scatter(agentslist[i]._x , agentslist[i]._y)
    #matplotlib.pyplot.scatter(agentslist[i].getx() , agentslist[i].gety())
matplotlib.pyplot.show()
 
'''
Find maximum and minimum distances between agents with no
repetition of pairs of agents and no testing against themselves
'''
range_start = 0
for i in range (range_start, number_of_agents - 1):
    for j in range (range_start + 1, number_of_agents):
        distances.append(distance_between (agentslist[i],agentslist[j]))
        range_start = range_start + 1
    #print("Distances: ", distances)
print ("Maximum Distance: ", max(distances))
print ("Minimum Distance: ", min(distances))




