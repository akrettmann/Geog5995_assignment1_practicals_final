#import operator
import matplotlib.pyplot
#import random
#import time

import csv
import matplotlib
import os

import agentframework6 as af

number_of_agents = 10
number_of_moves = 1000
agentslist = []

print("Initialise parameters:")
print("Number of agents ",number_of_agents)
print("Number of moves  ",number_of_moves)

environment = []
rowlist = []

#distances = []
#times_recorded = []

#Function to calculate the distance between agend a and agent b
#according to the Pythagoras' theorem
def distance_between_two_agents (a, b):
    return (((a.x - b.x)**2 + (a.y - b.y)**2)**0.5)

#Function to read the "environment data from the file <pathname> 
#relative path including filename) into the 2D environment list
#wherby each row of <pathname> will be stored as a rowlist in the 2D list.
def read_in_data_from_file (environment, pathname):
    #Open file and read data into list of lists
    f = open(pathname, newline='') 
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader: 
        rowlist = []
        for value in row: # A list of value
            rowlist.append(value)
        #print (rowlist)
        environment.append(rowlist)
    f.close()
    return environment

    
def write_outputfile(inputlist, pathname):
    #open and, if necessary, create output file 
    f = open(pathname,'w',newline='')
    #writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    writer = csv.writer(f, delimiter=' ', quoting=csv.QUOTE_NONNUMERIC)
    #writer.writerow(inputlist)
    for row in inputlist:
            writer.writerow(row)
            
    f.close()
    return 
#times_recorded = []
#for n in range(10,110,10):
    #start = time.process_time()
#number_of_agents = n
#print("number_of_agents", number_of_agents)

#Path of data file relative to directory of execution

#print(pathname)
#Initialise environment list with data about
#the spatial environment in which agents act
print("Initialise environment with data about the spatial environment from external file ")
environment = read_in_data_from_file (environment, "in.txt")

#print("output ",pathname)
#write_outputfile(environment, pathname)


#Generate Agents
print("Generate agents. ")
for i in range(number_of_agents):
    agentslist.append(af.Agent(environment))
    
#Moving and Eating Agents
print("Moving agents and consumption of environment")
for j in range (number_of_moves):  
    for i in range (0,number_of_agents):
        agentslist[i].move()
        agentslist[i].eat()
    #print("Display information about location and stores of agents")
    #print(agentslist[0].__str__(), environment[0][0])
    

matplotlib.pyplot.ylim(0,len(environment[0]))
matplotlib.pyplot.xlim(0,len(environment))
matplotlib.pyplot.imshow(environment)
for i in range (number_of_agents):
    matplotlib.pyplot.scatter(agentslist[i].x , agentslist[i].y)
        #matplotlib.pyplot.scatter(agentslist[i].getx() , agentslist[i].gety())

#Write out environment to the file out.csv
print("Write out the environment to the file out.csv")
# path of data file relative to directory of execution

write_outputfile(environment, "out.csv") 

#Calculate total amount of store by all agents and append to the file out.
print("calculate total amount of store by all agents and append this to the file out2.txt")
total=0
for a in agentslist:
    total += a.store
print("Total store: ", total)   
 
#Append total to the file out2.txt

with open ("out2.txt", "a") as f2:
    f2.write(str(total) + "\n")
    f2.flush
f2.close




