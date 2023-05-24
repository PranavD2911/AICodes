def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the minimum element with the first element of the unsorted array
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

# Example usage
input_array = list(map(int, input("Enter the elements of the array: ").split()))
sorted_array = selection_sort(input_array)
print("Sorted array:", sorted_array)
