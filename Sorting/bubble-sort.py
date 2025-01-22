# Bubble sort 
# Time complexity is O(n*n)

def bubbleSort(array, size): 
    for i in range(size-1):
        swapped = False
        for j in range(size-i-1):
            print(i, j)
            if array[j] > array[j+1]:
                swap(array, j, j+1)
                swapped = True
        
        if not swapped:
            break 

def swap(array, i, max_index):
    temp = array[max_index]
    array[max_index] = array[i]
    array[i] = temp


#arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
arr = [9,13,20,7,6,30]
size = len(arr)
bubbleSort(arr, size)
print('The array after sorting in Ascending Order by bubble sort is:')
print(arr)
