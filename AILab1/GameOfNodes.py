# -*- coding: utf-8 -*-
"""

@author: Ashley Abernathy
"""

import csv
import matplotlib.pyplot as plt

import networkx as net

from JonSnow import ucsJS
from WhiteWalker import ucsWW


pos = {} # stores city positions
dist = {} # stores the distances (weight) of the edges
edges = [] #stores the edges

with open('data.csv') as file:
     dataFile = csv.reader(file, delimiter = ',')
        # if second value in csv is int, add pos dict, else add edge dict
     for row in dataFile:
         if str.isdigit(row[1]):
             pos[row[0]] = (int(row[1]), int(row[2]))
         else:
             dist[(row[0], row[1])] = int(row[2])
             edges.append(','.join(row))

# create networkx graph using the edges generated from the csv file
nodeMap = net.parse_edgelist(edges, delimiter=',', data=(('weight', int),))
    
# Map the nodes
fig = plt.figure(figsize=(18, 14))

img = plt.imread("GoTMap2.png")
fig.add_subplot()
plt.imshow(img)
# draw the city positions with labels
net.draw_networkx(nodeMap, pos=pos, node_color = 'pink', font_size = 14, label=pos)

# add distances to the map with labels
net.draw_networkx_edge_labels(nodeMap, pos=pos, edge_labels=dist, font_size=12, label_pos=.5)
    
#add edges
net.draw_networkx_edges(nodeMap, pos=pos, width=2.0)
    
plt.title('Game of Nodes Map', fontsize = 24)
plt.legend(['City', 'Distance'], fontsize = 20)
plt.show()

ww = ucsWW(nodeMap, 'The Wall')

print(ww)

print("  ")

js = ucsJS(nodeMap, 'Trader Town', 'The Wall')

print(js)
