# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 17:34:59 2022

@author: simon
"""
import numpy as np
import json
from Square import Square

class Grid:
    
    def __init__(grid, row=5, column=5, time=0, name="Default"):
        
        if row < 1 or column < 1:
            raise NameError("Invalid grid size")
        if time < 0:
            raise NameError("Invalid time")

        grid.row = row;
        grid.column = column
        grid.time = time
        grid.name = str(name)
        
        tempGrid = np.empty(row*column, dtype=object);
        for i in range(row*column):
            tempGrid[i] = Square()  
        grid.matrix = tempGrid.reshape(row,column)
                
        
    def row(grid):
        return grid.row
    
    def column(grid):
        return grid.column
    
    def time(grid):
        return grid.time
    
    def name(grid):
        return grid.name
    
    def matrix(grid):
        return grid.matrix

    
    def grid(grid):
        return(grid.matrix)
    
    def content(grid, row, column):
        return grid.matrix[row][column].content
    
    def populateSquare(grid, row, column, value):
        grid.matrix[row][column].addContent(value)
        return grid;
    
    def deleteContentFromSquare(grid,row,column,value):
        grid.matrix[row][column].deleteContent(value)
    
    def print(grid):
        print ("Name: ", grid.name, "\n Time: ", grid.time)
        for row in range(grid.row):
            for col in range (grid.column):
                print(" |",grid.matrix[row][col].content, end = '')
            print(" |\n")
            
    def listOfContent(grid):
        coordsAndValues = []
        for x in range(grid.row):
            for y in range(grid.column):
                if len(grid.content(x,y)) > 0:
                    coordsAndValues.append([[x,y],grid.content(x,y)])            
        return coordsAndValues
                
    def toJson(grid):
        gridContent = {
                       'row' : grid.row, 
                       'column' : grid.column, 
                       'time' : grid.time, 
                       'name' : grid.name, 
                       'content' : grid.listOfContent()    
                       }
        return json.dumps(gridContent)