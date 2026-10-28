def find_pos():
    arr = [1, 3, 5, 5, 5, 7, 9, 11]
    target=5
    left=0
    right=len(arr)-1
    first=-1
    last=-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            first=mid
            right=mid-1
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            last=mid
            left=mid+1
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return first,last

    
ans=find_pos()
print(ans)        
    
