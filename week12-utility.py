def PrintOutout(word):
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
        
