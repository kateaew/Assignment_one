# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 07:53:18 2022
@author: Kate Warn
"""

import matplotlib.pyplot
import random
import agentframework
import csv
import os
import glob
import PIL

num_of_agents = 100
num_of_iterations = 10
neighbourhood = 20
random_seed = 0 

# This is the save location of the .GIF which is produced from running this code.
image_dir = 'C:/Users/katie/Documents/University_of_Leeds/YEAR_3/Programming/final1'

agents = []
environment = []
frames = []

# Read in the environment.
# This .txt file sets out the environment for the agents to move in
# It is a spatial file which creates a 'world' for the agents
print("Read environment.")
f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)
        #print(value)
    environment.append(rowlist)
f.close() 

# Make the agents.
# This creates the agents in a random way
print("Make the agents")
for i in range(num_of_agents):
    random_seed += 1
    agents.append(agentframework.Agent(environment, agents, random_seed))
print("Agents created")

# Move the agents.
# This moves the agents entirely randomly for a certain number of iterations
# The iterations can be changed by the user to change the way the agents act
# It also assigns a colour to the agents
print("Move the agents")
for j in range(num_of_iterations):
    random.shuffle(agents)
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y,color=agents[i].col)
    matplotlib.pyplot.savefig(image_dir+str(j)+'.png')
    matplotlib.pyplot.clf()
    print("Agents have been moved")
        
# Create animation
# This creates a .GIF file containing the movements of each agent
# It also shows the parts they have eaten in their environment
print("Create animation")
imgs=glob.glob(image_dir+"*.png")
for i in imgs:
    new_frame = PIL.Image.open(i)
    frames.append(new_frame)

frames[0].save('AgentsAndEnvironment.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=300, loop=0)
print("Animation created")

# Write out the environment to dataout.csv
# Writes out the environment data to a CSV file
print("Write out environment")
f2 = open('dataout.csv', 'w', newline='')
writer = csv.writer(f2, delimiter=' ')
for row in environment:
    writer.writerow(row)
f2.close()
print("Environment written out")

# Total amount stored by all agents
# This is a calculation to show how much has been stored or eaten by each agent
# It's then written out to a CSV file
print("Write out total stored")
total = 0
for a in agents:
    total += a.store
    #print(total)

file = os.path.join('dataout2.txt')
with open(file, "a") as f3:
    f3.write(str(total) + "\n")
    f3.write("\n")
    f3.flush  
f3.close
print("Total stored written out")

print("Process completed. Thank you for running this programme.")
