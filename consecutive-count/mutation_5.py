def consecutive_count(nums):
    '''
    =+ instead of +=
    '''
    count = 0
    for n in range(len(nums)-1):
        if nums[n] == nums[n+1]:
            count =+ 1
    return count