def find_peak_ele():
    arr=[1,2,3,1]
    left=0
    right=len(arr)-1
    found=-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]<arr[mid+1]:
            found=arr[mid+1]
            left=mid+1
        else:
            right=mid-1
    print(found)
find_peak_ele()
