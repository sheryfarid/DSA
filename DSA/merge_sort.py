def mergesort (arr):
    if len(arr) <= 1 :
        return arr
    mid = len(arr) // 2 
    left_half = arr[:mid]
    right_half = arr[mid:]
    return merge(mergesort(left_half), mergesort(right_half))

def merge(left,right):
    new = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i += 1 
        else:
            new.append(right[j])
            j += 1
    new.extend(left[i:])
    new.extend(right[j:])
    return new 

element = [453,4,223,453,234]
print(mergesort(element))
