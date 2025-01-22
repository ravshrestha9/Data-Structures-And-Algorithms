# Insertion sort 
# Time complexity is O(n*n)
def insertionSort(array, size):
    for i in range(size):
        j = i
        while (j > 0 and array[j-1] > array[j]):
            swap(array, j, j-1)
            j = j -1


def swap(array, i, min_index):
    temp = array[min_index]
    array[min_index] = array[i]
    array[i] = temp


arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(arr)
insertionSort(arr, size)
print('The array after sorting in Ascending Order by insertion sort is:')
print(arr)
