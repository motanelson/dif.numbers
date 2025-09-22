def vdif(a,b):
    return a/b
def difs(arra1):
    difint=[]
    for n in range(0,len(nps)-1):
        difint=difint+[nps[n+1]-nps[n]]
    return difint
def sums(arr1):
    l=len(arr1)
    s:float=0
    for n in range(l):
        s=s+arr1[n]
    return l,s
def predict(arra1):
    a=difs(arra1)
    c,b=sums(a)
    d=vdif(float(b),float(c))
    e=int(arra1[len(arra1)-1]+d)
    return e
def backpredict(arra1):
    a=difs(arra1)
    c,b=sums(a)
    d=vdif(float(b),float(c))
    e=int(arra1[0]-d)
    return e
def generation(froms,tos,lens):
    a=(tos-froms)/lens
    b=[]
    for n in range(int(froms),int(tos),int(a)):
        b=b+[int(n)]
    return b

backa=25
froma=50
toa=100
lena=10
print("\033c\033[43;30m\n")
nps=generation(froma,toa,lena)
print(froma,toa,lena)
print(nps)
l,ll=sums(difs(nps))
l=ll/l
print(l)
a=(froma-backa)/l
print(a)
npa=generation(backa,froma,a)
print(npa)
npa=npa+nps
print(npa)