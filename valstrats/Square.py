# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 18:23:28 2022

@author: simon
"""

class Square:
    
    def __init__(square, content=[]):
        if (len(content) == 0):
            square.content = []
        else:
            square.content = content
            
        
    def content(square):
        return square.content
    
    def addContent(square,value):
        for i in value:
            square.content.append(i)
        return True
    
    def deleteContent(square,value):
        for i in value:
            square.content.remove(i)