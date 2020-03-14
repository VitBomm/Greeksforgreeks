# Given an array A of N integers. The task is to find a peak element in it in O( log N ) .
# An array element is peak if it is not smaller than its neighbours. For corner elements, we need to 
# consider only one neighbour.
# Note: There may be multiple peak element possible, in that case you may return any valid index.

# Input:
# The first line of input contains an integer T denoting the number of test cases. Then T test cases follow.
#  Each test case contains an integer N. Then in the next line are N space separated values of the array.

# Output:
# For each test case output will be 1 if the index returned by the function is an index with peak element.

# User Task:
# You don't have to take any input. Just complete the provided function peakElement() and return the valid index.

# Constraints:
# 1 <= T <= 100
# 1 <= N <= 10
# 1 <= A[] <= 10

# Example:
# Input:
# 2
# 3
# 1 2 3
# 2
# 3 4
# Output:
# 1
# 1

# Explanation:
# Testcase 1: In the given array, 3 is the peak element as it is greater than its neighbour.
# Testcase 2: 4 is the peak element as it is greater than its neighbour elements.
# https://practice.geeksforgeeks.org/problems/peak-element/1

# your task is to complete this function
# function should return index to the any valid peak element
def findPeakUtil(arr, low, high, n):
     # Find index of middle element 
     # (low + high)/2  
    mid = low + (high - low)/2 
    mid = int(mid)
    # Compare middle element with its  
    # neighbours (if neighbours exist) 
    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid])):
        return mid
  
  
    # If middle element is not peak and  
    # its left neighbour is greater  
    # than it, then left half must  
    # have a peak element 
    elif (mid > 0 and arr[mid - 1] > arr[mid]): 
        return findPeakUtil(arr, low, (mid - 1), n) 
  
    # If middle element is not peak and 
    # its right neighbour is greater 
    # than it, then right half must  
    # have a peak element 
    else: 
        return findPeakUtil(arr, (mid + 1), high, n) 
  
  
# A wrapper over recursive  
# function findPeakUtil() 
def findPeak(arr, n): 
    return findPeakUtil(arr, 0, n - 1, n) 

arr = [1, 3, 20, 4, 1, 0]
n = len(arr)
print(arr[findPeak(arr, n)])