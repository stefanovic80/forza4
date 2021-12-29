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

#https://thispointer.com/python-how-to-find-all-indexes-of-an-item-in-a-list/
def get_index_positions(list_of_elems, element):
    ''' Returns the indexes of all occurrences of give element in
    the list- listOfElements '''
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            # Search for item in list from indexPos to the end of list
            index_pos = list_of_elems.index(element, index_pos)
            # Add the index position in list
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break
    return index_pos_list



r = 0
coordX = [] #initializate x coordinate of each circle
coordY = [] #initializate y coordinate of each circle
colors = ['red', 'blue'] # colors of circles
y = [1 for k in range(6)] #initializate y position of each circles

while r < 7:   
    coord = plt.ginput(n = 1)[0][0] #it takes x axis (second [0]) on forza4
    coord = np.round(coord)# it rounds to the closest integer
    coordX = coordX + [int(coord)]#list of x coordinates
    
    j = coordX[-1] - 1 # j is the index of a list and starts from 0 (not from 1)
    if coordX[-1] in coordX[:-1]:   
        y[j] = y[j] + 1
    
    print(j)
     
    coordY = coordY + [y[j]]#list of y coordinates
    dots, = ax.plot(coordX[r], y[j],\
                           'o', markersize=22, color = colors[r%2])
    plt.ginput(n = 1) #click two times before circle appearing
    r = r + 1
    
    odd_blue = [y for x,y in enumerate(coordX) if x%2 != 0]
    odd_blueY = [y for x,y in enumerate(coordY) if x%2 != 0]
    
    even_red = [y for x,y in enumerate(coordX) if x%2 == 0]
    even_redY = [y for x,y in enumerate(coordY) if x%2 == 0]
    
    #for t in range(6):
    t = 2
    print(get_index_positions(odd_blue, t) )
    print(get_index_positions(odd_blueY, t) )
    print(get_index_positions(even_red, t))
    print(get_index_positions(even_redY, t))