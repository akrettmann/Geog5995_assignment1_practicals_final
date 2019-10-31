import random
import matplotlib.pyplot
import matplotlib.animation
import agentframework8 as af
import csv

'''
When running this code in spider change the grafic
backend by typing '%matplotlib qt' in the IPython console.
To change the backend back to 'inline' type '%matplotlib inline'.
'''

'''
Reading in the environment from the file 'in.txt' which is
assumed to be in the current working directory.
'''
with open('in.txt') as csv_file:
    csv_read=csv.reader(csv_file, delimiter=',')
    environment=[]
    for row in csv_read:
        row_list=[]
        for value in row:
            row_list.append(int(value))
        environment.append(row_list)

number_of_agents = 20
number_of_iterations = 100
distance_of_neighbourhood = 50
random_seed = 0
agents = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


'''
 Make the agents
'''
for i in range(number_of_agents):
    random_seed += 1
    agents.append(af.Agent(environment, agents, random_seed))
#    print(len(agents[0].agentslist))


'''
Display a minimum number of frames before stopping criteria applies
'''
carry_on = True
minimum_number_of_frames = 50

def update(frame_number):

    fig.clear()
    global carry_on
    global minimum_number_of_frames
    for j in range(number_of_iterations):
        for i in range(number_of_agents):

            agents[i].move()
            agents[i].eat()
            agents[i].share(distance_of_neighbourhood)
        random.shuffle(agents)

    if random.random() < 0.1:
        carry_on = False
    '''
    When the global variable <carry_on> is set to False, the animation
    may still continue if the minimum number of frames have not been animated
    '''

    for i in range(number_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        #print(agents[i][0],agents[i][1])
    matplotlib.pyplot.imshow(environment)

def gen_function():
#def gen_function(b = [0]):
    a = 0
    global carry_on
    global minimum_number_of_frames
    while (carry_on or a < minimum_number_of_frames):
        yield a			# Returns control and waits next call.
        a = a + 1
    '''
    The stopping conditions have been met when:
        1.: the variable <carry_on> ist set to False and
        2.: the minimum number of frames have been animated
    '''
    print("stopping condition reached")

animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

matplotlib.pyplot.show()
