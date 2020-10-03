# Input:
# 2
# 9
# 2 3 4 -1 -2 1 5 6 3
# 10
# 1 0 0 1 -1 -1 0 0 1 0
# Output:
# 4
# 4

a = int(input())
for _ in range(a) :
    count = 0 
    arr1 = []
    n = int(input())
    arr = list(map(int,input().split()))
    for i in range (n) :
        if arr[i] > -1 :
            count +=1 
            arr1.append(count)
        else :
            count = 0 
            arr1.append(0)
    print (max(arr1))
    print (arr1)