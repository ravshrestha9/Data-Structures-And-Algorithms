# Quick sort 
# Time complexity is O(n*nlogn)
def quickSort(array, low, high):
    if low < high:
        partition_index = getPartition_index(array, low, high)
        quickSort(array, low, partition_index -1)
        quickSort(array, partition_index + 1, high)
    
def getPartition_index(array, low, high):
    i, j = low, high
    pivot = array[low]
    while (i<j):
        while (array[i] <= pivot and i < high):
            i+=1
        while (array[j] > pivot and j > low):
            j-=1
        if (i<j):
            swap(array, i, j)
    swap(array, low, j)    
    return j

def swap(array, i, j):
    temp = array[j]
    array[j] = array[i]
    array[i] = temp


arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
low = 0
high = len(arr) - 1
quickSort(arr, low, high)
print('The array after sorting in Ascending Order by insertion sort is:')
print(arr)