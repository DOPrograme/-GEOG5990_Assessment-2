# -*- coding: utf-8 -*-
"""
Created on Tue May 12 18:05:02 2022

@author: doujialiang
"""

import itertools
import random

class Drunks:
    
    # house=iter(list(range(10,260,10)))
    # #print(house)
    # house_number = next(house)
    # print(house_number)
    # while True:
    #     try:
    #         # get next value:
    #         x = next(house)
    #         print(x)
    #     except StopIteration:
    #         # Exit the loop when StopIteration is encountered
    #         break
 
    def __init__(self,environment,drunks,drunks_startx,drunks_starty,path,density):
        
        self.environment=environment
        self.drunks=drunks
        self.x=drunks_startx
        self.y=drunks_starty
        
        self.path={(self.x,self.y)}
        #print(self.path)
        
        house=iter(list(range(10,260,10)))
        #print(house)
        house_number = next(house)
        #print(house_number)
        self.house_number=house_number
        
        self.density=density
    
    def move(self,environment):
        
        if random.random()<0.5 and self.environment[self.x][self.y]!=1:
            self.x=(self.x+12)%len(self.environment[0])
        else:
            self.x=(self.x-12)%len(self.environment[0])
            
        if random.random()<0.5 and self.environment[self.x][self.y]!=1:
            self.y=(self.y+12)%len(self.environment)
        else:
            self.y=(self.y-12)%len(self.environment)
        
        #print(self.environment)
        self.path.add((self.x,self.y))
        #print(self.path)
            
    def steps(self, density):
        self.density[self.x][self.y] +=1 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        