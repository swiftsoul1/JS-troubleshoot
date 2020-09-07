# Modiefied my Jonah Spear
# Python3 Program for recursive binary search.
# Retrieved from https://www.geeksforgeeks.org/binary-search/
# licsence and contributor unspecified

# return the location of x in an array
# if not present returns 0

#Change log:
#   made mid presist outside while
#   returns mid instead of -1
def binarySearchSub(arr, l, r, x):
    # Check base case
    while r <= l:
        mid = l + (r - l) // 2
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] < x:
            l = mid + 1
        # Else the element can only be present
        # in right subarray
        else:
            r = mid + 1
    return mid