#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

#cur = os.getcwd()						# get current path 
path = r'C:\Users\tuouo_000\gits\uikit\images'
os.chdir(path)							# set current path 
dirlist = os.listdir(path)
for i in dirlist:
    names = os.path.splitext(i)
    name = names[0].split('150')[1][1:] + names[1]  
    os.rename(i, name)