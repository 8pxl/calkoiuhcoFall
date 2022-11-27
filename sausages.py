T = int(input())

def solve():
    line = input().split()
    n = int(line[0])
    k = int(line[1])

    highest = list(map(int,input().split()))
    lowest = list(map(int,input().split()))

    maxx = max(highest)
    minn = min(lowest)
    per = [0] * (maxx-1)
    for b in range(n):
        for c in range(minn,maxx):
            if c >= lowest[b] and c+1 <= highest[b]:
                per[c-1] += 1
                
    for d in range(len(per)):
        for e in range(len(per)-d):
            if(sum(per[e:e+1+d]) == k):
                print(e+1, e+1+d+1)
                return;


    print("IMPOSSIBLE")

for a in range(T):
    solve()