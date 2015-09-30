#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os 
'''
Only under os.path.abspath('.'), a file can be distinguish as file.
'''

def selectCondition(fileName, toFind, opt, path = '.'):
    flag = False
    if opt == 'name':
        if toFind == fileName.split('.')[0]:
            flag = True
        elif toFind == fileName:
            flag = True
    elif opt == 'pattern':
        flag = True if toFind in fileName else False
    elif opt == 'suffix':
        flag = True if toFind == fileName.split('.')[-1] else False
    elif opt == 'size':
        flag = True if toFind == os.path.getsize(path) else False
    return flag

def findFileFirst(toFind, root = '.', opt = 'name'):
    dirlist = os.listdir(root)
    for x in dirlist:
        path = os.path.join(root, x)
        if os.path.isfile(path) and selectCondition(x, toFind, opt, path):
            print(path)
    for x in dirlist:
        path = os.path.join(root, x)
        if os.path.isdir(path):
            findFileFirst(toFind, path, opt)

def findFileOrder(toFind = 'txt', root = '.', opt = 'name'):
    dirs = []
    for x in os.listdir(root):
        path = os.path.join(root, x)	
        if os.path.isfile(path) and selectCondition(x, toFind, opt, path):
            print(path)		
        elif os.path.isdir(path):	
            dirs.append(path)
    for dir in dirs:
        findFileOrder(toFind, dir, opt)

def findFileFirstByPattern(pattern = 'txt', root = '.'):
    findFileFirst(pattern, root, 'pattern')

def findFileFirstByName(name = '', root = '.'):
    findFileFirst(name, root, 'name')

def findFileFirstBySuffix(suffix = 'txt', root = '.'):
    findFileFirst(suffix, root, 'suffix')

def findFileOrderByPattern(pattern = 'txt', root = '.'):
    findFileOrder(pattern, root, 'pattern')

def findFileOrderByName(name = '', root = '.'):
    findFileOrder(name, root, 'name')

def findFileOrderBySuffix(suffix = 'txt', root = '.'):
    findFileOrder(suffix, root, 'suffix')

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
#test_find(findFileFirstBySuffix)
#test_find(findFileOrderByPattern)
#test_find(findFileOrderByName)
#test_find(findFileOrderBySuffix)

def findFileFirstBySuffix(size = '58464', root = '.'):
    findFileFirst(size, root, 'size')

def findFileOrderByPattern(size = '58464', root = '.'):
    findFileOrder(size, root, 'size')

def test_find_size(func):
    func(58464, r'C:\soft')		#\Inconsolata

#test_find_size(findFileFirstBySuffix)
#test_find_size(findFileOrderByPattern)