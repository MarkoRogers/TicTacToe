
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    k = 0
    numx = []
    for i in range(0, len(nums)-1):
        if nums[i] == nums[i + 1]:
            continue
        else:
            numx.append(nums[i])
            k += 1
    if nums[len(nums)-1] not in numx:
        numx.append(nums[len(nums)-1])
        k+=1
    numx += [0]*k
    nums = numx
    return k, nums
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

