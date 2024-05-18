# extract values from a sorted list

# subroutines if any, go here

# your subroutine goes here
def extract(list, lo, hi):
    if list is None:
        return None

    result = []

    low_index = binary_search(list, lo, True)
    high_index = binary_search(list, hi, False)
    result = list[low_index: high_index + 1]
    
    return result


def binary_search(arr, target, lowerbound):
    if target is None:
        return 0 if lowerbound else len(arr) - 1
    
    low, high = 0, len(arr) - 1
    result = -1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            result = mid
            if lowerbound:
                high = mid - 1
            else:
                low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    if lowerbound:
        return low
    else:
        return high
