def threeSumClosest(nums, target):
    final = float('inf')
    final_s = float('inf')
    if len(nums) < 3:
        return []
    nums = sorted(nums)
    for i, num in enumerate(nums):
        l = i + 1
        r = len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            temp = s - target
            if temp == 0:
                return s
            elif temp < 0:
                temp = temp * -1
                l += 1
            else:
                r -= 1
            if final > temp:
                final = temp
                final_s = s

    return final_s

nums = [-1, 2, 1, -4]
target = 1
closest_int = threeSumClosest(nums, target)
print(closest_int)
