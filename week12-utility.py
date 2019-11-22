#
#Bumsoo Kim
#CSCI102- Sec E
#Week 12 part B

def PrintOutput(word):
    print(word)
def LoadFile(file):
    with open (file, "r") as f:
        return [line.strip('\n') for line in f]
def UpdateString(string, sub, loc):
    st = string
    li = []
    for x in range (len(st)):
        li.append(st[x])
    li[loc] = sub
    print("OUTPUT ", end='')
    for z in range(len(li)):
        print(li[z], end='')
def FindWordCount(a, word):
    num = 0
    for n in range (len(a)):
        if a[n] == word:
            num +=1
    return num
            
def ScoreFinder(players, scores, name):
    loc = 0
    tof = len(players)
    name = name.upper()
    for m in range(len(players)):
        players[m] = players[m].upper()
        if players[m] == name:
            loc = m
            tof = tof **2
            
        else:
            tof -= 1
            
    sc = scores[loc]
    if tof == 0:
        print("OUTPUT player not found")
    else:
        print ("OUTPUT ", name, " got a score of ", sc)

def Union(scores, players2):
    for c in players2:
        scores.append(c)
    return scores
def Intersection(players, players2):
    nli=[]
    for q in players:
        for p in players2:
            if p == q:
                nli.append(q)
    return nli
def NotIn(players2, players):
    rli=[]
    blis=players2
    for v in blis:
        for w in players:
            if w == v:
                rli.append(v)
    for r in range(len(rli)):
        blis.remove(rli[r])
    print(t1, t2)
    return blis

                
                
    
    
