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
        r = simulate(days, j, d)[0]
        if r > most:
            most = r

    print(most)