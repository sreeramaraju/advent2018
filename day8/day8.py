#!/usr/bin/python

input = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'

class Node(object):
    def __init__(self):
        self.child = []
        self.data = []

vals = input.split()

def build_tree(index=0):
    tree = Node()
    tree.child = [Node()] * int(vals[index])
    tree.data = [0] * int(vals[index+1])
    index = index + 2
    for i in range(len(tree.child)):
        t, index = build_tree(index)
        tree.child[i]=t
    for i in range(len(tree.data)):
        tree.data[i] = int(vals[index])
        index = index + 1
    return tree, index

def sumVal(tree):
    v = sum(tree.data)
    for c in tree.child:
        v += sumVal(c)
    return v

def trickySum(tree):
    v = 0
    if len(tree.child) == 0:
        v += sum(tree.data)
    else:
        for d in tree.data:
            if len(tree.child) >= d:
                v += trickySum(tree.child[d-1])
    return v

def main():
    print("Welcome Day8")
    input = '' 
    with open('input', 'r') as f:
        for l in f:
            input = l
    global vals
    vals = input.strip().split()
    t, i = build_tree(0)
    print(sumVal(t))
    print(trickySum(t))

    
if __name__ == "__main__":
    main()
