def maxArea(height):
    max_area, l, r = 0, 0, len(height) - 1
    while l < r:
        temp = min(height[l], height[r])
        max_area = max(temp * (r - l), max_area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_area

height = [1,8,6,2,5,4,8,3,7]
max_area = maxArea(height)
print('Max Area with most water:',max_area)