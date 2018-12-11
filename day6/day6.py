#!/usr/bin/python

from collections import defaultdict

input = ( (1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9))

def boundaries(input):
    x, y = 0, 0
    for i,j in input:
        x = max(x,i)
        y = max(y, j)
    return x, y

#
# distance = 0
# while (points)
#  For each point
#    ps = get points at distance i 
#           and with in boundary 
#           and not marked
#    if touched boundary unmark   
#    if ps is empty remove from points
#    for each point
#      if map[ps] != nil
#           map[ps] = .            
#      map[ps] = point
#      map[point] += 1 
#   
#    distance++
#     
#

def mark_areas(boundaries, input=input):
    x,y,(l,h) = 0,0,boundaries
    print(x,y,l,h)
    distance = 0
    pointsMap = defaultdict()
    for i in input:
        pointsMap[pointsMap]=pointsMap
    
    while()

def main():
    print("Welcome to Day6")
    x, y = boundaries(input)
    mark_areas( (x,y) ) 

if __name__ == '__main__':
    main()
