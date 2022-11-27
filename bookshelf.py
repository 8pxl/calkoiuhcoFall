T = int(input())

for i in range(T):
    dim = list(map(int, input().split()))
    shelves = list(map(int, input().split()))

    N = dim[0]
    B = dim[1]
    W = dim[2]
    D = dim[3]

    shelf = 0
    shelfArea = 0

    for s in shelves:
        shelf += s
        shelfArea += (s * W * D)

    total = ( (2 * B) + W) * D * (((len(shelves) + 1)* B) + shelf)   

    print(total - shelfArea)
