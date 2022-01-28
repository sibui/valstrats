# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 19:35:22 2022

@author: simon
"""

from Grid import Grid
from os.path import exists
import json

class Strat:
    
    def __init__(strat,fileName =""):
        if not (fileName == ""):
            if not exists(fileName): raise NameError("File doesn't exist")
            with open(fileName) as json_file:
                data = json.load(json_file)
            numGrids = data['size']
            grids = []
            for i in range(numGrids):
                gridData = json.loads(data['grids'][i])
                row = gridData['row']
                col = gridData['column']
                time = gridData['time']
                name = gridData['name']
                grids.append(Grid(row,col,time,name))
                
                content = gridData['content']
                for j in range(len(content)):
                    squareData = content[j]
                    sRow = squareData[0][0]
                    sCol = squareData[0][1]
                    sContent = squareData[1]
                    grids[i].populateSquare(sRow, sCol, sContent)
                    #print(squareData)
            strat.grids = grids
        else:
            strat.grids = []
        
    def grids(strat):
        return strat.grids;
        
    def addGrid(strat, grid):
        strat.grids.append(grid)
        
    def print(strat):
        for grid in strat.grids:
           grid.print()
           
    def toJson(strat):
        stratbook = json.loads(json.dumps({'grids':[],'size':len(strat.grids)}))
        for i in range(len(strat.grids)):
            stratbook['grids'].append(strat.grids[i].toJson())
        return stratbook 
        
    def saveToFile(strat,name="ValStrat"):
        jsonStrat = strat.toJson()
        with open(name+'.json', 'w') as outfile:
            json.dump(jsonStrat, outfile)
    
 
        