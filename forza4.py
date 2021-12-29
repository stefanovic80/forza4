# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import pandas as pd
#import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab

import matplotlib 

import numpy as np
#%matplotlib qt#notebook
plt.close()
plt.ion()

matplotlib.rc('xtick', labelsize=14) 
matplotlib.rc('ytick', labelsize=14) 

plt.rcParams['lines.linewidth'] = 3
#plt.rcparam['axes.grid'] = True 

import warnings
warnings.filterwarnings('ignore')



font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 14}

matplotlib.rc('font', **font)

fig = plt.figure(figsize = (5, 3))
ax = fig.add_subplot(111)
ax.set_xlim(.5, 6.5)
ax.set_ylim(.5, 6.5)
for u in range(0, 6, 1): 
    ax.vlines(u + .5, -.5, 6.5)
    ax.hlines(u + .5, -.5, 7)

r = 0
coordX = []
coordY = []
colors = ['red', 'blue']
dots = []
j = 0
y = [1 for k in range(6)] #[1, 1, 1, 1, 1, 1]

while r < 8:   
    coord = plt.ginput(n = 1)[0][0] #it takes x axis (second [0]) on forza4
    coord = np.round(coord)# it rounds to the closest integer
    coordX = coordX + [int(coord)]
    
    j = coordX[-1]
    if coordX[-1] in coordX[:-1]:     
        y[j] = y[j] + 1
     
    coordY = coordY + [y[j]]
    dots, = ax.plot(coordX[r], y[j],\
                           'o', markersize=22, color = colors[r%2])
    
    r = r + 1
    print(y)