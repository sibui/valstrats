# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 19:35:22 2022

@author: simon
"""

from Grid import Grid

class Strat:
    
    def __init__(strat):
        strat.grids = []
        
    def grids(strat):
        return strat.grids;
        
    def addGrid(strat, grid):
        strat.grids.append(grid);
        
    def print(strat):
        for grid in strat.grids:
           grid.print();
        
    