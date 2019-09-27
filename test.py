def binarySearch(arr, l, r, x):
    # Check base case
    if r >= l:

        mid = l + (r - l) // 2

        # If element is present at the middle itself 
        if arr[mid] == x:
            return mid

            # If element is smaller than mid, then it can only
        # be present in left subarray 
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

            # Else the element can only be present in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array 
        return -1

list_val =[0,1,2,3,4,7,8,9,10]
low = 0
high = len(list_val)-1
answer = binarySearch(list_val, low, high, 4)

print (answer)
