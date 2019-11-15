# -*- coding: utf-8 -*-
"""
This is for Jon Snow using Uniform Cost Search
This is to find the quickest route to his goal.

John Snow's goal is to reach the white walkers as
they leave the wall
@author: Ashley
"""
import queue as que

def ucsJS(nodeMap, start, goal):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            
            if node == goal:
                #return current visited list when back at the wall
                return visited

            for neighbor in nodeMap[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    #return visited

