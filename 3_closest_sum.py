def threeSumClosest(nums, target):
    nums.sort()
    closest = float('inf')
    for i in range(len(nums)):
        left=i+1
        right=len(nums)-1
        while left<right:
            current_sum=nums[i]+nums[left]+nums[right]
            if abs(current_sum - target) < abs(closest - target):
                closest = current_sum
            if current_sum>target:
                left+=1
            elif current_sum<target:
                right-=1
            else:
                return current_sum
    return closest
nums=[-1,2,1,-4]
res=threeSumClosest(nums, 1)
print(res)
