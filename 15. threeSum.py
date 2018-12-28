def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    m = 0
    d = {}
    if len(nums) < 3:
        return []
    nums = sorted(nums)
    for i, num in enumerate(nums):
        l = i + 1
        r = len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                t = (nums[i], nums[l], nums[r])
                if t not in d:
                    d[t] = 1
                if nums[l] == nums[r]:
                    break
                l += 1
                r -= 1
    return [*map(list, d.keys())]


nums = [-1,0,1,2,-1,-4]
list_of_list = threeSum(nums)
print('Three Sums:', list_of_list)