def minWindow(arr):
    n=len(arr)
    low=0
    high=n-1
    while arr[low]<=arr[low+1]:
        low+=1
        if low==n-1:
            return 0
    while arr[high]>=arr[high-1]:
        high-=1
    sub_min=min(arr[low:high+1])
    sub_max=max(arr[low:high+1])
    while arr[low-1]>sub_min:
        low-=1
    while arr[high+1]<sub_max:
        high+=1
    return high-low+1
arr=[1,2,5,3,7,10,9,12]
res=minWindow(arr)
print(res)
