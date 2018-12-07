#!/usr/bin/python

input = ( (1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9))

def boundaries(input):
    x, y = 0, 0
    for i,j in input:
        x = max(x,i)
        y = max(y, j)
    return x, y

def mark_areas(boundaries, input=input):
    print(boundaries)
    print(input)

def main():
    print("Welcome to Day6")
    x, y = boundaries(input)
    mark_areas( (x,y) ) 

if __name__ == '__main__':
    main()
