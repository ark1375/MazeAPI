# A-Star
# CostFunction -> g(n)
## (0,0) -> (1,0) : Cost = 1

# HuresticFunction -> h(n)
## (0,0) -> (12,2) : Cost = 14 , Huresic =/= 18  ==>  h <= c
##
## Manhatan Distance  v,p -> L1-Norm (vp)   (x_p - x_v) + (y_p - y_v)
## Euclidian Distance  v,p  -> L2-Norm(vp)  sqrt( (x_p - x_v)**2 + (y_p - y_v)**2)

# EstimationFunction -> f(n) = g(n) + h(n)

import math
import examp_maze
import numpy as np
import time

def hurestic( point_a:tuple  , point_b:tuple , type:int = 2) -> float:
    
    assert type > 0 and type < 3 , 'Invalid number for type'
    
    # (x,y)
    if type == 1:
        return abs( (point_a[0] - point_b[0]) + (point_a[1] - point_b[1]) ) 

    elif type == 2:
        return abs( math.sqrt(
            (point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2
        ) )

    return None


def estimate(point_a:tuple  , point_b:tuple, cost:int , type:int = 2):
    return hurestic(point_a , point_b , type ) +  cost


MAZE = np.array(examp_maze.MAZE)

START = (15,1)
GOAL = (15,29)

# Node = [name , hurestic , cost , father , estimate]
# DICT => HashMap

class Node(object):

    def __init__(self , name:tuple ,  father):
        self.name = name
        self.father = father
        self.hurestic = hurestic(name , GOAL)


        if not father:
            self.cost = 1
        else:
            self.cost = father.cost + 1

        self.estimate = estimate(name , GOAL , self.cost )

    def __repr__(self):
        return str(self.name)

    def __bool__(self):
        return True

    def expand(self, maze) -> list:

        expansion_list = []

        ## You have to lookup all 4 sides
        north = self.name[0] - 1 , self.name[1]
        east = self.name[0] , self.name[1] + 1
        west = self.name[0] , self.name[1] - 1
        south = self.name[0] + 1 , self.name[1]

        ## Take into consideration the boundaries of maze

        if maze[north] == 0 and (north != self.father.name):
            north_node = Node(north , self)
            expansion_list.append(north_node)

        if maze[south] == 0 and (south != self.father.name):
            south_node = Node(south , self)
            expansion_list.append(south_node)

        if maze[west] == 0 and (west != self.father.name):
            west_node = Node(west , self)
            expansion_list.append(west_node)

        if maze[east] == 0 and (east != self.father.name):
            east_node = Node(east , self)
            expansion_list.append(east_node)

        return expansion_list


dumy_father = Node((-1,-1) , None)
start_node = Node(START , dumy_father)

node_list = [start_node]

for elm in start_node.expand(MAZE):
    print(
        elm.father
    )


while node_list:
    time.sleep(0.01)
    current_node = node_list.pop()

    print( f'{current_node.name} ==> {current_node.hurestic}' )

    if current_node.name == GOAL:
        print('You reached your destination !!!!')
        break

    node_list.extend(
        current_node.expand(MAZE)
    )

    node_list.sort(key=lambda x : x.estimate , reverse=True)
    


## Take in note that the loop might be a problem