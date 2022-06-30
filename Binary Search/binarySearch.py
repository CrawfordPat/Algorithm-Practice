import random

def binarySearch(searchArray, target):
    bottomLimit = 0
    topLimit = len(searchArray) + 1

    mid = bottomLimit + (topLimit - bottomLimit) // 2

    while mid != target:
        if mid > target:
            topLimit = mid
            mid = bottomLimit + (topLimit - bottomLimit) // 2
        
        elif mid < target:
            bottomLimit = mid
            mid = bottomLimit + (topLimit - bottomLimit) // 2

        else:
            return -1
            
    return mid
