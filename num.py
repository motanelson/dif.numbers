print("\033c\033[43;30m\n")
nps=[]
nps=[1,2,3,4,5,6,7,8,9]
difint=[]
for n in range(0,len(nps)-1):
    difint=difint+[nps[n+1]-nps[n]]
print(nps)
print(" "+str(difint))