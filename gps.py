import pygame
from pygame.locals import *
from vector import Vector2
from constants import *
import numpy as np
from node import *
visited = []
queue = []
nodesLUT = None
def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)