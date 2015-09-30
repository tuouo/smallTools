#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os 
'''
Only under os.path.abspath('.'), a file can be distinguish as file.
'''

def selectCondition(dirname, toFind, opt):
    flag = False
    if opt == 'name':
        if toFind == dirname.split('.')[0]:
            flag = True
        elif toFind == dirname:
            flag = True
    elif opt == 'pattern':
        flag = True if toFind in dirname else False
    elif opt == 'suffix':
        flag = True if toFind == dirname.split('.')[-1] else False
    return flag

def findFileFirst(toFind, root = '.', opt = 'name'):
    dirlist = os.listdir(root)
    for x in dirlist:
        path = os.path.join(root, x)
        if os.path.isfile(path) and selectCondition(x, toFind, opt):
            print(path)
    for x in dirlist:
        path = os.path.join(root, x)
        if os.path.isdir(path):
            findFileFirst(toFind, path, opt)

def findFileOrder(toFind = 'txt', root = '.', opt = 'name'):
    dirs = []
    for x in os.listdir(root):
        path = os.path.join(root, x)	
        if os.path.isfile(path) and selectCondition(x, toFind, opt):
            print(path)		
        elif os.path.isdir(path):	
            dirs.append(path)
    for dir in dirs:
        findFileOrder(toFind, dir)

def findFileFirstByPattern(pattern = 'txt', root = '.'):
    findFileFirst(pattern, root, 'pattern')

def findFileFirstByName(name = '', root = '.'):
    findFileFirst(name, root, 'name')

def findFileOrderByPattern(pattern = 'txt', root = '.'):
    findFileOrder(pattern, root, 'pattern')

def findFileOrderByName(name = '', root = '.'):
    findFileOrder(name, root, 'name')

def test_find(func):
    func('.md')
    print("End of one findding.")
    func('md')
    print("End of one findding.")
    func('otf', r'C:\soft')
    print("End of one findding.")
    func('.gitconfig', r'C:')
    print("End of one findding.")
    func('pdf', 'C:\\Users\\tuouo_000\\Documents\\其它')
    print()

#test_find(findFileFirstByPattern)
#test_find(findFileFirstByName)
#test_find(findFileOrderByPattern)
#test_find(findFileOrderByName)