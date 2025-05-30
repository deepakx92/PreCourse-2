# Python program for implementation of Quicksort Sort 
# Time complexity - O(n log n)
# Space complexity - O(1)
# Did the problem ran on leetcode - Yes
# Problems faced - mulitple problems - needs revision
  
# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    t = arr[i + 1]
    arr[i + 1] = pivot
    arr[high] = t
    return i + 1
    

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        p = partition(arr, low, high)
        quickSort(arr, low, p - 1)
        quickSort(arr, p + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
