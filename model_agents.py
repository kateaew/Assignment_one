# -*- coding: utf-8 -*-
"""
Created on Mon July 4 15:39:12 2022

@author: katie
"""

import random
import operator
import matplotlib.pyplot
import agentframework


def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5


num_of_agents = 10
num_of_iterations = 100
agents = []


# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent())

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()


matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show()


for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        
