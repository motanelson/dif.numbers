
def saves(names):
    nps=[]
    f1=open(names,"r")
    s=f1.read()
    f1.close()
    npss=s.split(",")
    for n in npss:
        nps=nps+[int(n.strip())]
    return nps  
print("\033c\033[43;30m\n")
nps=saves("data.txt")
nps.sort()
print(nps)