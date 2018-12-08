#!/usr/bin/python

from collections import defaultdict

def parseInput():
    graph = defaultdict(set)
    with open("input1",'r') as f:
        for l in f:
            res = l.split(' ')
            graph[res[7]].add(res[1])
            if res[1] not in graph:
                graph[res[1]] = set()
    return graph
            

def free_tasks(g):
    free = []
    for k in g.keys():
        if len(g[k]) == 0:
            free.append(k)
    for k in free:
        g.pop(k)
    return free

def clean_up(elem, g):
    for k in g.keys():
        if elem in g[k]:
            g[k].remove(elem)
    

def printTopSort(g):
    free = []    
    result = ''
    while(len(g) > 0 ):
        free.extend(free_tasks(g))
        free.sort()
        fElem = free[0]
        result += fElem
        free = free[1:]
        clean_up(fElem, g)
    return result
        


def main():
    print("Welcome to Day7")
    g = parseInput()
    #print(g)
    res = printTopSort(g)
    print(res)

if __name__ == "__main__":
    main()
