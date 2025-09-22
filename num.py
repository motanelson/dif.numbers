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

print("\033c\033[43;30m\n")
nps=[]
nps=[1,2,3,4,5,6,7,8,9]

print(nps)
d=difs(nps)
print(" "+str(d))
l,n=sums(d)
print(n/l)
