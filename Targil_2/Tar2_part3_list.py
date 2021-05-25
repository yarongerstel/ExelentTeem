def count_evens(nums):
    c=0
    for i in nums:
        if i%2==0:
            c+=1
    return c

def big_diff(nums):
    mn=nums[0]
    mx=0
    for i in range(len(nums)):
        mn=min(mn,nums[i])
        mx=max(mx,nums[i])
    return mx-mn

def centered_average(nums):
    mn = nums[0]
    mx = 0
    l=[]
    for i in range(len(nums)):
        mn = min(mn, nums[i])
        mx = max(mx, nums[i])
    nums.remove(mn)
    nums.remove(mx)
    return sum(nums) / len(nums)

def sum13(nums):
    while 13 in nums:
        i = nums.index(13)
        nums.remove(nums[i])
        if(i<len(nums)):
            nums.remove(nums[i])
    return sum(nums)


def sum67(nums):
    while 6 in nums:
        i = nums.index(6)
        while nums[i] != 7 and i <= len(nums):
            nums.remove(nums[i])
            if nums[i] == 7:
                nums.remove(nums[i])
                break
    return sum(nums)

def sum22(nums):
    while 2 in nums:
        i = nums.index(2)
        nums.remove(nums[i])
        if i<len(nums) and nums[i]==2:
            return True
    return False





