import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import matplotlib 
import numpy as np

plt.close()
plt.ion()

fig = plt.figure(figsize = (5, 3))
ax = fig.add_subplot(111)
ax.set_xlim(.5, 6.5)
ax.set_ylim(.5, 6.5)
for u in range(0, 6, 1): 
    ax.vlines(u + .5, -.5, 6.5)
    ax.hlines(u + .5, -.5, 7)


r = 0
coordX = [] #initializate x coordinate of each circle
coordY = [] #initializate y coordinate of each circle
colors = ['red', 'blue'] # colors of circles
y = [1 for k in range(6)] #initializate y position of each circles

breakOuterLoop = 0
while breakOuterLoop == 0:   
    coord = plt.ginput(n = 1)[0][0] #it takes x axis (second [0]) on forza4
    coord = np.round(coord)# it rounds to the closest integer
    coordX = coordX + [int(coord)]#list of x coordinates
    
    j = coordX[-1] - 1 # j is the index of a list and starts from 0 (not from 1)
    if coordX[-1] in coordX[:-1]:   
        y[j] = y[j] + 1
     
    coordY = coordY + [y[j]]#list of y coordinates
    dots, = ax.plot(coordX[r], y[j],\
                           'o', markersize=22, color = colors[r%2])
    plt.ginput(n = 1) #click two times before circle appearing
    r = r + 1
    
    coordsX = []
    coordsY = []
    #[0] is even, which is red. [1] is odd, which is blue
    
    coordsX = coordsX + [ [y for x,y in enumerate(coordX) if x%2 == 0] ]
    coordsY = coordsY + [ [y for x,y in enumerate(coordY) if x%2 == 0] ]

    coordsX = coordsX + [ [y for x,y in enumerate(coordX) if x%2 != 0] ]
    coordsY = coordsY + [ [y for x,y in enumerate(coordY) if x%2 != 0] ]

    t = 0
    #winner = 0
    for winner in range(2):
        try:
            loop_end = max(coordsY[winner]) + 1
            while t < loop_end:
                k = [b for a, b in zip(coordsY[winner], coordsX[winner]) if a == t]
                #k = np.array(even_red)[indRedY].tolist() # select only
                k.sort()
                print(t)
                print(loop_end)
                try:
                    g = min(k)
                    if (len(k)> 3) and (k == [g, g + 1, g +2, g + 3]):
                        print("The winner is " + colors[winner])
                        breakOuterLoop = 1
                        break
                
                except:
                    pass
                
            t +=1
        except:
            pass
        