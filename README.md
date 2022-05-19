# GEOG5990_Assessment-2

Introduction

The motivation behind this project was to fulfil the requirements for the final assignment of the GEOG5995 Programming for Social Scientists: Core Skills [Python] course at Leeds University. The requirements of the project were given as:

    Pull in the data file and find out the pub point and the home points.
    Draw the pub and homes on the screen.
    Model the drunks leaving the pub and reaching their homes, and store how many drunks pass through each point on the map.
    Draw the density of drunks passing through each point on a map.
    Save the density map to a file as text.
    
The project folder name is Assessment2 which contains following files   
1. drunk.plan.txt: 1 raster file (300 by 300 pixels) indicating the pub point and homes. From the top left to the bottom right of the raster file, one line per image line is used. The bar is represented by one, the dwellings by tens, and the empty spaces by zeros. There are 25 inebriated people (house numbers 250, 240, 230...etc...10).
2. drunk_Agents.py: file containing the drunk class
3. drunk_model.py: The body code to run the model, , which contains the main functions of the Agents.
4. density.txt:  This is automatically generated after running the model which can show density map.

How to run the model

To run this model in Spyder the files must be in the same directory and the graphics backend for the IPython console should be set to "Tkinter".
The model is run via the file (drunk_model.py)

What the model does

Agent:
drunks: These are our basic agents that interact with the environment and with each other.
Set the bar's position to their starting point, every update they move, check the value represented by their location, and record their path (row and column numbers passed). If their location represents a value that is exactly equal to the number of their house, show home
They are drawn in white in our animation.
The drunks class has three functions. Firstly, a constructor function (init) allows the initialisation of the attributes of the class, which are environment, drunks, pubx, puby, density. Another function is the ‘move’ function, which uses the random library to move the agents up, down, left, or right within the boundaries of the environment, depending on the outcome of the random number. The self.path attribute records where the agent has been. The last function, steps, records the density of the agents passing through the cells. 

The drunk model loads the drunks class first. It also includes matplotlib.pyplot for plotting the final model, as well as the csv library for reading raster files and writing out the density map as a txt file. The integer value of num of drunks is set to 25 and the location of pubx, puby is set to 0. Density, environment, drunks, and path are all set up as empty lists at first. The drunk.plan.txt file is appended to the environment list using the csv.reader (from the csv library), with each row filled with values from the file. The drunk.plan.txt file is read a second time, appended to the density list, and filled with values of 0 in each row — this is what will be used to track the path of agents going through.

Model outputs

When the model pauses, it's safe to conclude that either all of the drunks have returned home or the maximum number of iterations has been reached.


License

This project is licensed under the MIT License - see the LICENSE.md file for details

Acknowledgemnts

Many thanks to Dr. Andy Turner for providing the material for the course and to him and his teaching assistants for the delivery of the course.
