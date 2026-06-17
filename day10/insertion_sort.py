def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>= 0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
            arr[j+1]=key
    return arr
arr=[64,23,11,24,1]
sorted_arr=insertion_sort(arr)
print("sorted array is:",sorted_arr)        