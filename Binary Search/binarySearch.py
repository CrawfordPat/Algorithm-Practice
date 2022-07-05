import random

def binarySearch(searchArray, target):
    bottomLimit = 0
    topLimit = len(nums)-1

    while bottomLimit <= topLimit:
        mid = bottomLimit + (topLimit - bottomLimit) // 2

        if nums[mid] < target:
            bottomLimit = mid + 1
        elif nums[mid] > target:
            topLimit = mid - 1
        else:
            return mid
    return -1
