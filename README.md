# Assignment 1, GEOG5995M Programming for Social Science

Agent based model of agents interacting on resources within an environment

### About

This series of practicals implements an agent based model acting in an environment by consuming the resources of the environment while randomly moving around within the dimensions of the environment. The agents "know" of each other and also share resources.

The series of practicals is designed to gradually build up Python programming skills by using the program development environment Spyder. The agent based model is build up gradually accordingly starting with rather simple exercises and step by step adding more complex processing features such as object classes, reading and writing csv and html files (web scraping), and building graphical user interfaces (GUI).

The model takes in a raster input file consisting of 300 rows and 300 columns of integer values to be taking as an environment grid of (y,x) coordinates in which agents (e.g. sheeps) and resources (e.g. grass) are placed. The numbers in the grid represent the amount of resource units and the location of an agent is represented by its corresponding coordinates. The agents move randomly around the grid and consume and/or share resources according to some rules.

The agents are implemented as an object class with methods like 'move', 'eat' and 'share'.

### Installation and Execution

The series of programs and raster input file 'in.txt' can be accessed from the following Github repository:
https://github.com/akrettmann/Geog5995_assignment1_practicals_final

The files for each practical are stored in a separate folder. In order to execute a practical all associated files need to be in the same folder, including the raster input file if applicable.

The main programs of each folder can be executed in the Spyder development environment. The practicals that require arguments on execution should be called on command line level, but provide default arguments such that the program also works in Spyder. For the parameter sweeping exercise subprocess calls are used.  

The animation practicals require a change in backend. In order to run practical8 in Spyder issue the command '%matplotlib qt' in the Spyder console. To reverse this change issue the command '%matplotlib inline' after the execution finished. Practical9 requires Tkinter to be set as the graphical backend.

### Authors

These practicals have been completed by Anna Krettmann as part of Assignment 1, GEOG5995 Programming for Social Science. 

### License

The license can be found at: https://github.com/akrettmann/Geog5995_assignment1_practicals_final

