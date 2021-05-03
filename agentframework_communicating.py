# -*- coding: utf-8 -*-
"""
Created on Fri May 15 07:53:18 2020

@author: Kate Warn
"""

import random
 
class Agent():
    def __init__ (self, environment, agents, random_seed):
        self.environment = environment
        self.agents = agents
        random.seed(random_seed)
        self.store = 0
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)

    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
        print(str(self.store))
        if self.store > 100:
            self.environment[self.y][self.x] = self.environment[self.y][self.x] + 100
            print(str(self))
            self.store = 0
            print(str(self))
            self.__str__.__call__
            print("Location x =", self.x, "y =", self.y, "store =", str(self.store))

    def share_with_neighbours(self, neighbourhood):
        print(neighbourhood)
        for agent in self.agents:
            if(self != agent):
                dist = self.distance_between(agent) 
                if dist <= neighbourhood:
                    sum = self.store + agent.store
                    ave = sum /2
                    self.store = ave
                    agent.store = ave
                    print("sharing " + str(dist) + " " + str(ave))

    def __str__(self):
        return "Location x = " + str(self.x) + ", y = " + str(self.y) + ", store = " + str(self.store)
    
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5 
