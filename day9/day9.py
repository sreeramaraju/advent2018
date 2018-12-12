#!/usr/bin/python

from collections import defaultdict

score = defaultdict(int)
players = 9 

def playi1(marble):
    global score
    global players
    if marble == 1:
        return [0,1], 1
    marbles, curr_marble = play(marble-1)
    if marble%23 == 0:
        score[marble%players] += marble
        score[marble%players] += marbles.pop(curr_marble-7)
        return marbles, curr_marble-7
    if curr_marble + 1 == len(marbles):
        curr_marble = -1
    new_index = (curr_marble+2)
    marbles.insert(new_index, marble)
    return marbles, new_index

def play(marble):
    global score
    global players
    marbles = [0,1]
    curr_index = 1
    if marble == 1:
        return marbles, curr_index 
    
    for i in range(2,marble+1):
        if i%23 == 0:
            print(i)
            #print(i, len(marbles), curr_index)
            curr_index -= 7
            if curr_index < 0:
                curr_index = len(marbles) - abs(curr_index)
            score[i%players] +=i
            score[i%players] += marbles.pop(curr_index)
            if curr_index == len(marbles):
                curr_index = 0
        else:
            if curr_index + 1 == len(marbles): #if last Index
                curr_index = 1
            else:
                curr_index += 2
            marbles.insert(curr_index,i)
    return marbles, curr_index

def main():
    print("Day 9")
    global score
    global players
    marbles = 72170*100 
    players = 470 
    #marbles = 25 
    a, b = play(marbles)
    print(sorted(score.values()))

if __name__ == "__main__":
    main()
