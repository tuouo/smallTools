#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Only under os.path.abspath('.'), a file can be distinguish as file.
'''
import os 

def findFileFirst(toFind, root = '.', opt = 'name'):
    dirlist = os.listdir(root)
    for x in dirlist:
        path = os.path.join(root, x)
        flag = False
        if opt == 'name':
        	flag = True if toFind == x.split('.')[0]
        if os.path.isfile(path) and flag:
            print(path)
    for x in dirlist:
        path = os.path.join(root, x)
        if os.path.isdir(path):
            findFileFirst(toFind, path)

def findFileOrderByPattern(pattern = 'txt', root = '.'):
    dirs = []
    for x in os.listdir(root):
        path = os.path.join(root, x)	
        if os.path.isfile(path) and pattern in x:	# os.path.isfile(path), path not x
            print(path)		
        elif os.path.isdir(path):	
            dirs.append(path)
    for dir in dirs:
        findFile(pattern, dir)

def findFileFirstByPattern(pattern = 'txt', root = '.'):
    dirlist = os.listdir(root)
    for x in dirlist:
        path = os.path.join(root, x)
        if os.path.isfile(path) and pattern in x:
            print(path)
    for x in dirlist:
        path = os.path.join(root, x)
        if os.path.isdir(path):
            findFileByPattern(pattern, path)

def findFileFirstByName(name, root = '.'):
    dirlist = os.listdir(root)
    for x in dirlist:
        path = os.path.join(root, x)
        if os.path.isfile(path) and name == x.split('.')[0]:
            print(path)
    for x in dirlist:
        path = os.path.join(root, x)
        if os.path.isdir(path):
            findFileFirstByName(name, path)

def test_find(func):
    func('.txt')
    print("End of one findding.")
    func('Except')
    print("End of one findding.")
    func('otf', r'C:\soft')
    print("End of one findding.")
    func('pdf', 'C:\\Users\\tuouo_000\\Documents\\其它')
    print()

test_find(findFileOrderByPattern)
#test_find(findFileFirstByPattern)
#test_find(findFileFirstByName)