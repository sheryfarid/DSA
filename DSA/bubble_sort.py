
def bubblesort(l1):
    n = len(l1)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if l1[j] > l1[j+1]:
                l1[j] , l1[j+1] = l1[j+1] ,l1[j]
                swapped = True
        if not swapped:
            break
    return l1




element = [23,565,334,35,234,23]
# element = ["shery","uzair", "hammad", "talha","ali"]
print(bubblesort(element))







