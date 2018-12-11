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

def clean_up(elems, g):
    for k in g.keys():
       g[k] = g[k] - set(elems)

#  define list with fixed length
#  default sort by value and reset the value as time proceeds
#  
#
#
#

def printTopSort(g, parallel=1):
    free = []    
    result = ''
    while(len(g) > 0 ):
        free.extend(free_tasks(g))
        free.sort()
        fElems = process(free, parallel)
        clean_up(fElems, g)
        result += "".join(fElems)
    return result


workers = []
time_taken = 0

def process(tasks, parallel=1):
    global workers
    global time_taken
    # add
    for t in tasks[0:parallel-len(workers)]:
        tasks.pop(0)
        workers.append( (t,ord(t)-4 + time_taken))
    # sort
    workers.sort(key=lambda x:x[1])    
    # pop
    min = workers[0][1]
    time_taken = min
    done = []
    while(len(workers)>0 and min == workers[0][1]):
        done.append(workers.pop(0)[0])
    return done    
    # pick tasks equal to empty slots
    # store as (task, val)
    # find the tasks with min val
    # substract minval from all tasks and pop 0 val tasks

def main():
    print("Welcome to Day7")
    global time_taken
    g = parseInput()
    cG = g.copy()
    res = printTopSort(g, 1)
    print(res, time_taken, workers)
    time_taken = 0 
    res = printTopSort(cG, 5)
    print(res, time_taken, workers)



if __name__ == "__main__":
    main()
