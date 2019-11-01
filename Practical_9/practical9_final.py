import random
import operator
import matplotlib
matplotlib.use('TkAgg')
import tkinter
import matplotlib.pyplot
import matplotlib.animation
import agentframework9 as af
import csv
import requests
import bs4

#Reading in the environment
with open('in.txt') as csv_file:
    csv_read=csv.reader(csv_file, delimiter=',')
    environment=[]
    for row in csv_read:
        row_list=[]
        for value in row:
            row_list.append(int(value))
        environment.append(row_list)

number_of_agents = 10
number_of_iterations = 100
distance_of_neighbourhood = 50
random_seed = 0
agents = []

'''
Scraping web data from the HTML file data.html in order to
initialise the model with x and y coordinates contained in
data.html which can be accessed through the link
http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html
'''

'''
Query the website and return the HTML data to the variable ‘r’.
'''
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
'''
Parse the HTML data using BeautifulSoup and store in variable `soup`.
'''
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
#print(td_ys)
#print(td_xs)
print("Extracting the yx-coordinates from the HTML source")
ycoordinates = []
xcoordinates = []
for y in td_ys:
    print(y.text)
    ycoordinates.append (y.text)
for x in td_xs:
    xcoordinates.append(x.text)
for i in range(len(ycoordinates)):
    print("YX-coordinates: ", ycoordinates[i], "  ",xcoordinates[i])

'''
Initialise graphical user interface.
Generate new figure object.
'''
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

carry_on = True


def update(frame_number):

    fig.clear()
    global carry_on
    for j in range(number_of_iterations):
        for i in range(number_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share(distance_of_neighbourhood)
        # reshuffle the agentslist every time around to avoid artifacts
        random.shuffle(agents)
    for i in range(number_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
    matplotlib.pyplot.imshow(environment)

def gen_function(b = [0]):
    a = 0
    global carry_on
    while (carry_on) :
        yield a
        a = a + 1

def stop_function():
    global carry_on
    carry_on = False

def scale_function():
    global number_of_agents
    number_of_agents=agents_scale.get()

'''
Creating the function that will run the animated plot when clicked on in the menu.
Continues to update the plot until stopping criteria is met.
'''

def init_agents():
    global agents
    random_seed = 0

    for i in range(number_of_agents):
        j = i
        while (i > len(td_ys)): # ensure we don't fall off the end of the array
            j -= len(td_ys)
        y = int(td_ys[i].text)
        x = int(td_xs[i].text)
        # Add 5 to random seed to get each agent initialised and moving differently
        random_seed += 5
        agents.append(af.Agent(environment, agents, random_seed, y, x))

def run():
    global animation
    '''
    Initialise agents
    '''
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False, init_func=init_agents)
    canvas.draw()
'''
Creating the main window
'''
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

#add field section where users can enter the number of agents
agents_scale = tkinter.Scale(root, label="Number of Agents", from_=10, to=100,
                             orient=tkinter.HORIZONTAL)
agents_scale.pack()

#adding change value button
changevalue_button = tkinter.Button(root, text="adopt", command=scale_function)
changevalue_button.pack()

#adding stop button
stop_button = tkinter.Button(root, text="stop", command=stop_function)
stop_button.pack()

#adding exit button
exit_button = tkinter.Button(root, text="exit", command=root.destroy)
exit_button.pack()


tkinter.mainloop()
