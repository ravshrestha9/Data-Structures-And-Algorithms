# Selection sort 
# Time complexity is O(n*n)


def selectionSort(array, size):
    
    for i in range(size):
        print(i)
        min_index = i

        for j in range(i+1, size):
            print(j)
            print("---------------")
            if array[j] < array[min_index]:
                min_index = j
        
        swap(array, i, min_index)


def swap(array, i, min_index):
    temp = array[min_index]
    array[min_index] = array[i]
    array[i] = temp


arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by bubble sort is:')
print(arr)
