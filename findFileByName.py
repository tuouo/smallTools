#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os 
def findFile(pattern = 'txt', root = '.'):
    dirs = []
    for x in os.listdir(root):
        path = os.path.join(root, x)	
        if os.path.isfile(path) and pattern in x:	# os.path.isfile(path), path not x
            print(path)		
        elif os.path.isdir(path):	
            dirs.append(path)
    for dir in dirs:
        findFile(pattern, dir)

#findFile('.txt')
#print("End of one findding.")
#findFile('Except')
#print("End of one findding.")
#findFile('otf', r'C:\soft')
#print("End of one findding.")
#findFile('pdf', 'C:\\Users\\tuouo_000\\Documents\\其它')

