#!/usr/bin/python

def read_file(fname):
    claims = []
    with open(fname, 'r') as f:
        for l in f:
            claims.append(l.strip())
    return claims        

def parse_claim(c):
    claim = c.split(" ")[0][1:]
    dims = c.split("@ ")[1].split(": ")
    topleftoffset = dims[0].split(",")
    size  = dims[1].split("x")
    return claim, int(topleftoffset[0]), int(topleftoffset[1]), int(size[0]), int(size[1])
 

def dimentions(claims):
    w, h = 0, 0
    for c in claims:
        cno, x,y,w1,h1 = parse_claim(c)
        maxw, maxh = x + w1, y+h1 
        if w < maxw:
            w = maxw
        if h < maxh:
            h = maxh
    return w, h

def mark_claims(claims, cloth):
    marked = dict()
    doublemarked = dict()
    cleanClaimSet = set()
    overlapClaimSet = set()
    for c in claims:
        cno, x,y,w,h = parse_claim(c)
        clean = True
        for i in range(x,x+w,1):
            for j in range(y,y+h,1):
                if (i,j) in marked:
                    clean = False
                    overlapClaimSet.add(marked[(i,j)])
                    doublemarked[(i,j)] = 1
                marked[(i,j)] = cno
        if clean:
            cleanClaimSet.add(cno)
    return marked, doublemarked, cleanClaimSet-overlapClaimSet
def count_repeated_claims(cloth):
    pass

def main():
    print("Welcome to Day3")
    claims = read_file("input1")
    # print(claims)
    w, h = dimentions(claims)
    print(w, " ", h)
   
    fabric = [[0]*h for i in range(w)]
    m, dm, cleanClaims = mark_claims(claims, fabric)
    print(len(dm))
    print(cleanClaims)

if __name__ == '__main__':
    main()
