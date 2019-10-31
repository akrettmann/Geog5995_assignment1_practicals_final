#import operator
import matplotlib.pyplot
import random
#import time

import csv
import matplotlib
import os

import agentframework7 as af
#from sys import argv
import sys

agentslist = []
environment = []
rowlist = []

def str_to_bool(v):
    return v.lower() in ("yes", "true", "t", "1")

'''
STEP 1:     Initialise parameters

Read command line arguments and catch wrong user input. The programme
expects 5 arguments: 
    1. the name of the file containing the program
    2. the number of agents (integer value), 
    3. the number of iterations(integer value),
    4. the size of the neighbourhood (integer value), and
    5. the initial value for the randomisation sequence
    
Default values are assigned if not enough arguments are provided.
'''    
print("Initialise parameters:")

if len(sys.argv) < 6:
    print ("Not enough arguments ")
    print("Numner of arguments provided: ", len(sys.argv), " Number of Arguments needed: ", 5)
    print("1st argument: program file name including path")
    print("2nd argument: integer value for number of agents")
    print("3rd argument: integer value for number of iterations")
    print("4th argument: integer value for size of neighbourhood")
    print("4th argument: integer value for setting the random seed" )
    print("The program runs with the following default values: ")
    print("Number of Agents: ", 10)
    print("Number of iterations: ", 1000)
    print("Size of Neighbourhood: ", 20)
    print("Random Seed: ", 7)
    number_of_agents = 10
    number_of_moves = 1000
    neighbourhood = 20
    random_seed = 7
    visual_on = "yes"
elif len(sys.argv) > 6:
    print("More than 5 argument")
    print("Only the first 5 arguments are considered, the rest will be ignored")
else:
    number_of_agents = int(sys.argv[1])
    number_of_moves = int(sys.argv[2])
    neighbourhood = int(sys.argv[3])
    random_seed = int(sys.argv[4])
    visual_on = str(sys.argv[5])
    print ('Name of Program File":',  str(sys.argv[0]))
    print("Number of Agents: ", number_of_agents)
    print("Number of Agents: ", number_of_moves)
    print("Neighbourhood Size: ", neighbourhood)
    print("Random Seed: ", random_seed)
    print("Visual on: ", visual_on)
   



'''
STEP 2:     Initialise Environment


Initialise environment list with data about
the spatial environment in which agents act
'''
print("Initialise environment with data about the spatial environment from external file ")

'''
Read the environment data from  the file in.txt in the current working directory. 

The Data is read into the 2D environment list wherby each row of <inputfile> 
will be stored as a rowlist in the 2D list.
'''

    #Open file and read data into list of lists
with open("in.txt", newline='') as f: 
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader: 
        rowlist = []
        for value in row: # A list of value
            rowlist.append(value)
        #print (rowlist)
        environment.append(rowlist)


#for j range (len(environment)):
#print("Environment ",len (environment))

#print("output ",pathname)
#write_outputfile(environment, pathname)

'''
STEP 3:      Generate Agents
'''
print("Generate agents. ")
for i in range(number_of_agents):
    random_seed += 1
    agentslist.append(af.Agent(environment,agentslist, random_seed))
    #print("agentslist after initialising: ",agentslist)
 
'''
STEP 4:      Agents Acting
  
Agents acting: moving and consumption of environment (eating and sharing).
In order to avoid model artifacts the order in which the agents are processed
is changed at each iteration, i.e. the list of agents is shuffled before action
is performed.
'''
print("Moving agents and consumption of environment")
for j in range (number_of_moves): 
    random.shuffle (agentslist)
    for i in range (number_of_agents):
        agentslist[i].move()
        agentslist[i].eat()
        agentslist[i].share_with_neighbours(neighbourhood)
    #print("Display information about location and stores of agents")
    #print(agentslist[0].__str__(), environment[0][0])
    
'''
STEP 5:     Plotting agents in environment
'''
print ("Visual On: ", visual_on)
if str_to_bool(visual_on) :   
    print("Plotting agents in environment.")            
    matplotlib.pyplot.ylim(0,len(environment[0]))
    matplotlib.pyplot.xlim(0,len(environment))
    matplotlib.pyplot.imshow(environment)
    for i in range (number_of_agents):
        matplotlib.pyplot.scatter(agentslist[i]._x , agentslist[i]._y)
        #matplotlib.pyplot.scatter(agentslist[i].getx() , agentslist[i].gety())
    matplotlib.pyplot.show()
else:
    pass

'''
STEP 6:     Write out environment to the file out.csv
'''

print("Write out the environment to the file out.csv")
#Path of output file is relative to directory of execution directory

#Open and, if necessary, create output file 
with open("new_environment.csv",'w',newline='') as f2:
    #writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    writer = csv.writer(f2, delimiter=' ')
    #writer.writerow(inputlist)
    for row in environment:
        writer.writerow(row)
            

'''
STEP 7:    Calculate total amount of store by all agents and append to the file out2.
'''
print("Calculate total amount of store by all agents and append this to the file out2.txt")
total=0
for a in agentslist:
    total += a.store
print("Total store: ", total)   
 
#Append total to the file out2.txt
with open ("out.txt", "a") as f3:
    f3.write(str(total) + "\n")
    f3.flush





