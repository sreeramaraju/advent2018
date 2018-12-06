#!/usr/bin/python

def polymer(input, ignore=''):
    stack = []
    ignore = ignore.lower()
    for c in input:
        if c.lower() == ignore:
            continue
        val = stack[-1:]
        if len(val) > 0 and c.swapcase() == val[0]:
          #  print("c, val", c, val)
            stack.pop()
        else:
          #  print("else c, val", c, val)
            stack.append(c)
    return stack

def read_input(fname):
    input = ''
    with open(fname, 'r') as f:
        for l in f:
           input += l
    #print(input)
    return input.strip()

def answer1(input):
    s = polymer(input)
    print(len(s))

def answer2(input):
    all_polymers = []
    for c in 'abcdefghijklmnopqrstuvwxyz':
        all_polymers.append(len(polymer(input, c)))
    all_polymers.sort()
    print(all_polymers)

def main():
    print("Welome to Day5")
    input = read_input("input1")
    answer1(input)
    answer2(input)

if __name__ == '__main__':
    main()
