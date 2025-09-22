def generation(froms,tos,lens):
    a=(tos-froms)/lens
    b=[]
    for n in range(int(froms),int(tos),int(a)):
        b=b+[int(n)]
    return b

froma=50
toa=100
lena=10
print("\033c\033[43;30m\n")
nps=generation(froma,toa,lena)
print(froma,toa,lena)
print(nps)
