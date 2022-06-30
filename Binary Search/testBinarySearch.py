import random
import binarySearch

# Test the binary search function
def testBinarySearch():
    # make a random array of size 100
    array = []
    for i in range(100):
        array.append(random.randint(0, 100)) 

    # sort the array
    array.sort()

    # test the binary search
    testCounter = 0
    for i in range(1000):
        target = random.randint(1, 100)
        print(f"Searching for {target}")
        binarySearch.binarySearch(array, target)
        testCounter += 1
        print(f"{testCounter} tests completed successfully")

testBinarySearch()