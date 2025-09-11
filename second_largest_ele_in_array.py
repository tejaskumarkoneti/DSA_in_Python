def secondLargest(arr,n):
    # Check if array has less than 2 elements
    if len(arr) < 2:
        return -1
    
    # Initialize largest and second largest with negative infinity
    largest = float('-inf')
    secondlargest = float('-inf')

    # Iterate through the array
    for i in range(n):
        # If current element is larger than largest
        if arr[i] > largest:
            # Update second largest to previous largest
            secondlargest = largest
            # Update largest to current element
            largest = arr[i]
        # If current element is larger than second largest but not equal to largest
        elif arr[i] > secondlargest and arr[i] != largest:
            # Update second largest to current element
            secondlargest = arr[i]
            
    # Return second largest if found, otherwise return -1
    return secondlargest if secondlargest != float('-inf') else -1

# Test array
arr = [5,8,9,15,0,3]
# Get length of array
n = len(arr)
# Call function and print result
print("SecondLargest element in the array is ",secondLargest(arr,n))