def bubble(arr):
    size=len(arr)
    steps=[arr.copy()]
    swaps=0;comp=0
    for i in range(size):
        swapped=False
        for j in range(size-i-1):
            comp+=1
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                swaps+=1
                steps.append(arr.copy())
                swapped=True
        if not swapped:
            break
    return {
        "Algorithm":"Bubble Sort",
        "Sorted Array":arr,
        "Swaps":swaps,
        "Steps":steps
    }
