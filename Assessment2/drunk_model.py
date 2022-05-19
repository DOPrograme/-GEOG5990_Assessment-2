# -*- coding: utf-8 -*-
"""
Created on Tue May 12 04:35:06 2022

@author: doujialiang
"""

#import random
#import operator
#import drunk_Agents
import csv
import matplotlib.pyplot
import drunk_Agents
import matplotlib.animation
import tkinter
matplotlib.use('TkAgg')
num_of_iterations =300 

environment = [] # create a list for .txt as envrionment 
pubx=[]
puby=[]

drunks = []
path=[]
density=[]

drunk_startxs,drunks_starty=0,0
num_of_drunks=25

count=0

# read environment data which are pub points and houses
f = open('drunk.plan.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

for row in reader: # A list of rows make cvs file into it
    rowlist = []    
    for value in row: # A list of value
        rowlist.append(value)
    environment.append(rowlist)
f.close()

f = open('drunk.plan.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader: # A list of rows make cvs file into it
    rowlist = []    
    for value in row: # A list of value
        value=0
        rowlist.append(value)
    density.append(rowlist)
f.close()

# use matplotlib.pyplot.figure show houses
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
# matplotlib.pyplot.ylim(0,300)
# matplotlib.pyplot.xlim(0,300)
# matplotlib.pyplot.imshow(environment)   

# identify the pub in environment
for j, row in enumerate(environment):
    for i, value in enumerate(row):
        if value == 1:# the pubs value is 1
            pubx.append(i)
            puby.append(j)

# choose one of the pub points as a starting point for the drunks 
drunks_startx=pubx[221]
drunks_starty=puby[221]
            
#create drunks list
for i in range(num_of_drunks):
    #Pass the value in while calling drunk_Agents.py
    drunks.append(drunk_Agents.Drunks(environment,drunks,drunks_startx,drunks_starty,path,density))


def update(self):
    
    fig.clear()
     
    for i in range(num_of_drunks):
        
        #while(environment[drunks[i].x][drunks[i].y]!=drunks[i].house_number):
            
        if environment[drunks[i].x][drunks[i].y]==drunks[i].house_number:
            
            drunks[i].remove()
            global count          
            count+=1
            print("drunk reached home",count)
            if count==(num_of_drunks):
                print("All drunks reached home")
            
        else:
            #prevent backtracking
            if environment[drunks[i].x] not in path and environment[drunks[i].y] not in path:
                
                drunks[i].move(environment)
                drunks[i].steps(density)
        
        
        #Let 25 drunks go together
        # matplotlib.pyplot.ylim(0,300)
        # matplotlib.pyplot.xlim(0,300)
        # matplotlib.pyplot.imshow(environment)
        # matplotlib.pyplot.scatter(drunks[i].x,drunks[i].y,c="snow")

    matplotlib.pyplot.ylim(0,300)
    matplotlib.pyplot.xlim(0,300)       
    matplotlib.pyplot.imshow(density)
        
# for i in range(num_of_drunks):
#     update(drunks[i])

    # Export the density file as a txt file 
    with open('density.txt', 'w', newline='') as out_file:
        writer = csv.writer(out_file, delimiter=',')
        for row in density:
            writer.writerow(row)
    
#animation = matplotlib.animation.FuncAnimation(fig, update, interval=100,repeat=False, frames=num_of_iterations)               

def run(): #Function for generating animation
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=num_of_iterations, repeat=False)
    #animation = matplotlib.animation.FuncAnimation(fig, sim, frames=10, repeat=False)
    canvas.draw()
        
def Stop(): # function for stopping the model at it's defined conclusion
    global root
    root.quit()
    print('Model Completed!')
    
def terminate():  # Function to force quit model
    global root
    root.quit()
    root.destroy()

root = tkinter.Tk()    
root.wm_title("Drunks go home Model") #Set title

#Create canvas for drawing model
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# Create buttons which can call functions. 
run_button = tkinter.Button(root, text="Run Model", command=run) #button to start model
quit_button = tkinter.Button(root, text="Stop Model", command=terminate) #button to stop model
run_button.configure(bg='green') #colours start button green
quit_button.configure(bg='red') #colours stop button red
quit_button.pack(side=tkinter.BOTTOM) #locates stop button at bottom of gui
run_button.pack(side=tkinter.BOTTOM) #locates start button at bottom of gui


tkinter.mainloop() #load up GUI       