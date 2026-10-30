def find_perfect_sqr(n):
    arr=[]
    for ele in range(1,n+1):
        arr.append(ele)
    print(arr)
    left=0
    right=n-1
    found=-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]*arr[mid]<=n:
            found=arr[mid]
            left=mid+1
        elif arr[mid]*arr[mid] > n:
            right=mid-1
            
        else:
            left=mid+1
            found=arr[mid]
    print(found)
n=int(input("Enter a number:"))
find_perfect_sqr(n)
