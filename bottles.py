T = int(input())

def selectionSort(array, size):
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if array[j][1] < array[min_index][1]:
                min_index = j
                (array[ind], array[min_index]) = (array[min_index], array[ind])

for i in range(T):
    n = int(input())
    students = list(map(int,input().split()))
    for i in range(n):
        students[i] = (i,students[i])
    selectionSort(students,n)
    new = [x[0]+1 for x in students]
    total = 0
    for a in range(len(students)):
        total += students[a][1] * (len(students) - (a))
    print(total)
    for num in new:
        print(num, end = ' ')
    print()

