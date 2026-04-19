def sortedSqr(nums):
    result=[0,0,0,0,0]
    pos=4
    left=0
    right=len(nums)-1
    while left<=right:
        if abs(nums[left])<abs(nums[right]):
            result[pos]=nums[right]**2
            right-=1
            pos-=1
        else:
            result[pos]=nums[left]**2
            left+=1
            pos-=1
    return result
arr=[-4,-1,0,3,10]
res=sortedSqr(arr)
print(res)
