# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 18:23:28 2022

@author: simon
"""

class Square:
    
    def __init__(square):
        square.content = [];
        
    def content(square):
        return square.content;
    
    def addContent(square,value):
        square.content.append(value);
        return True;