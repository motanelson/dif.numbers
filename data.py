def multa(muls,lena):
    nps=[]
    for n in range(lena):
        nps=nps+[n*muls]
    return nps
def sadds(arra,nn):
    nps=[]
    for n in range(len(arra)):
        t=arra[n]+nn
        nps=nps+[t]
    return nps
def saves(names,arra):
    s=""
    for n in range(len(arra)):
        if n==0:
            s=str(arra[n])
        else:
            s=s+", "+str(arra[n])
    f1=open(names,"w")
    f1.write(s)
    f1.close()  
print("\033c\033[43;30m\n")
nps=multa(10,200)
print(nps)
nps=sadds(nps,30)
print(nps)
saves("data.txt",nps)