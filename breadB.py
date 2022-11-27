T = int(input())

def simulate(lst,index,days):
    bread = 0
    for i in range(days):
        if(index + i >= len(lst)):
            return(bread,0)
        if not lst[index + i] == 0:
            bread += lst[index + i]
        else: 
            return bread,days - i-1
    return(bread,0)


for i in range(T):
    n,k,d = list(map(int,input().split()))
    days = list(map(int,input().split()))

    most = 0

    for j in range(len(days)):
        r = ()
        d = 0
        pen = 0
        for l in range(k):
            r = simulate(days, l + pen, d)
            pen += r[1] + d
            d+=r[0]
    
        if d > most:
            most = d

    print(most)