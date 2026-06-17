def binary_search(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:  
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
arr=["e","g","k","m","p","s","u"]
target="m"
Idx=binary_search(arr,target)
print(f"Found at index {Idx} ") 