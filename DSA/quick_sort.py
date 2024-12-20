def quicksort(arr , low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quicksort(arr,low, pivot-1)
        quicksort(arr, pivot+1, high)

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1 
    j = high
    while True:
        while i <= j and arr[i] <= pivot:
            i +=1
        while i <= j and arr[j] >= pivot:
            j -=1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j 


element = [34,23,2,12,45]
quicksort(element, 0 ,len(element)-1)
print(element)
