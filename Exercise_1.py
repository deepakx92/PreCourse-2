# Python code to implement iterative Binary  
# Search. 

# Time Complexity - O(log n)
# Space Complexity - O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this - 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
    
    while l <= r: # l < r is incorrect, if there is only 1 element [5]
        mid = (l + r) // 2 # problem with this calculation earlier, Initially did l + r // 2   
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    
    return -1
  
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40, 50, 10] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result )
else: 
    print("Element is not present in array")
