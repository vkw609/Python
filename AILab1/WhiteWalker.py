# -*- coding: utf-8 -*-
"""
This is for White Walkers using Depth First Search
This is so that they may visit all the cities.

White Walkers visit all cities so they have no goal

@author: Ashley
"""

def ucsWW(nodeMap, start):
    visited = set()
    queue = [start]

    while queue:
        node = queue.pop()
        if node not in visited:
            visited.add(node)

            for city in nodeMap[node]:
                if city not in visited:
                    queue.append(city)
    return visited