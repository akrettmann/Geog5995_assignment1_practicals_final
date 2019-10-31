import random
import operator
import matplotlib.pyplot
import time

'''
Recording execution times with a variety of
different orders of magnitude of agent numbers
between 10 and 100.
'''
times_recorded = []
for n in range(10,110,10):
    start = time.process_time()
    agents = []
    distances = [] 
    number_of_agents = n
    number_of_iterations = 100

   
    def distance_between (agents_row_a, agents_row_b):
        if (type(agents_row_a) is not list) or (type(agents_row_b) is not list):
            print("argument to function is not of type list")
            return False
            
        return (((agents_row_a[0] - agents_row_b[0])**2 + (agents_row_a[1] - agents_row_b[1])**2)**0.5)
    '''
    Initialise all agents with random integers
    '''
    print("Initialise all agents with random integers")
    for i in range (number_of_agents):
        agents.append([random.randint(0,100),random.randint(0,100)])
        
    '''
    Initialise all agents with random integers
    '''    
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
        #print ("moved agents", agents, "iteration: ", j)
    
    #distance= ((agents[0][0] - agents[1][0]) ** 2 + (agents[0][1] -agents[1][1]) **2 ) **0.5
    #print ("moved agents", agents)
    #print ("Distance between agents", distance)
    
    #print ("Agent with largest x-coordinate", max(agents, key=operator.itemgetter(1)))
    print("Locations after ",number_of_iterations," number of moves")
    print (agents)
    
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
        #matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
    #else:
        #matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
    
    #matplotlib.pyplot.scatter(m[1],m[0],color='red')
    matplotlib.pyplot.show()

    '''
    Find maximum and minimum distances between agents with no
    repetition of pair of agents and no testing against themselves
    '''
    range_start = 0
    for i in range (range_start, number_of_agents - 1):
        for j in range (range_start + 1, number_of_agents):
            distances.append(distance_between (agents[i],agents[j]))
            #print("distance between ", agents[i], "and ", agents[j], " : ", distance_between_two_agents (agents[i],agents[j]))
            #print("distance between ", agents[i], "and ", agents[j], " : ",distances[-1] )
        range_start += 1
        #print("Distances: ", distances)
    print ("Maximum Distance: ", max(distances))
    print ("Minimum Distance: ", min(distances))
    end = time.process_time()
    #print("Execution time for ", number_of_agents, "agents was :", end - start)
    times_recorded.append([number_of_agents,end-start])

print("____________________________________________")
for i in range(len(times_recorded)):
    print("Execution time for ", times_recorded[i][0], "agents was: ",times_recorded[i][1])

