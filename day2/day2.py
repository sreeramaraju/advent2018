#!/usr/bim/python
from collections import defaultdict

def read_file(fname):
    boxes = []
    with open(fname, "r") as f:
        for l in f:
            boxes.append(l.strip())
    return boxes

def count2sAnd3s(code):
    cnt2, cnt3 = 0, 0
    c_d = defaultdict(int)    
    for c in code:
        c_d[c] += 1
    vals = c_d.values()
    if 2 in vals:
        cnt2 = 1
    if 3 in vals:
        cnt3 = 1
    return cnt2, cnt3    

def compare_prototypes(str1, str2):
    print(str1, " ", str2)
    val = None 
    if len(str1) != len(str2):
        return None
    for index, c in enumerate(str1):
        if c != str2[index]:
            if str1[index+1:] == str2[index+1:]:
                val = str1[0:index] + str1[index+1:]
            break
    return val
def findFabricProto(boxes):
    for i1 in range(0,len(boxes)):
        for i2 in range(i1+1,len(boxes)): 
            v = compare_prototypes(boxes[i1],boxes[i2])
            if v != None:
                print(i1,i2)
                return v

def main():
    codes = read_file("codes")
    cnt2, cnt3 = 0, 0
    for c in codes:
        x1, x2 = count2sAnd3s(c)
        cnt2 += x1
        cnt3 += x2
    print(cnt2,cnt3)
    print(cnt2*cnt3)

    protoboxes = read_file("input2")
    answer = findFabricProto(protoboxes)
    print(answer)


if __name__ == '__main__':
    main()  


