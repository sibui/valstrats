# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 17:34:59 2022

@author: simon
"""
import numpy as np
from Square import Square

class Grid:
    
    def __init__(grid, row=5, column=5, time=0, name="Default"):
        
        if row < 1 or column < 1:
            raise NameError("Invalid grid size")
        if time < 0:
            raise NameError("Invalid time")

        grid.row = row;
        grid.column = column;
        grid.time = time;
        grid.name = name;
        
        tempGrid = np.empty(row*column, dtype=object);
        for i in range(row*column):
            tempGrid[i] = Square();
        grid.matrix = tempGrid.reshape(row,column);
                
        
    def row(grid):
        return grid.row;
    
    def column(grid):
        return grid.column;
    
    def time(grid):
        return grid.time;
    
    def name(grid):
        return grid.name;
    
    def matrix(grid):
        return grid.matrix;

    
    def grid(grid):
        return(grid.matrix);
    
    def content(grid, row, column):
        return grid.matrix[row][column].content;
    
    def populateSquare(grid, row, column, value):
        grid.matrix[row][column].addContent(value);
        return grid;
    
    def print(grid):
        print ("Name: ", grid.name, "\n Time: ", grid.time)
        for row in range(grid.row):
            for col in range (grid.column):
                print(" |",grid.matrix[row][col].content, end = '')
            print(" |\n")