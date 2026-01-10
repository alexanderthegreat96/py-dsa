# The Coding Challenge: "Volume of Lakes"
# The Problem: Imagine you have an array of integers representing the heights of a series of vertical walls,
# each with a width of 1. If it rains, water will get trapped between the walls to form "lakes."
# Your Task: Write a function that takes an array of non-negative integers and returns the total volume
# of water trapped between the walls.

heights : list[int] = [0,1,0,2,1,0,1,3,2,1,2,1]

def volume_of_lakes(heights: list[int]) -> int:
    if not heights:
        return 0

    n = len(heights)
    left, right = 0, n - 1
    max_left, max_right = 0, 0
    total_water = 0

    while left < right:
        if heights[left] < heights[right]:
            # If current height is a new peak, update max_left
            if heights[left] >= max_left:
                max_left = heights[left]
            else:
                # Otherwise, it's a dip! Calculate water.
                total_water += max_left - heights[left]
            left += 1
        else:
            # If current height is a new peak, update max_right
            if heights[right] >= max_right:
                max_right = heights[right]
            else:
                # Otherwise, it's a dip! Calculate water.
                total_water += max_right - heights[right]
            right -= 1 # Corrected: move inward

    return total_water

print(f'Total volume of water trapped: {volume_of_lakes(heights)}')
