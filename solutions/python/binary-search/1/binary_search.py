"Find the Value in the search list using Binary Search"
def find(search_list, value):
    "find the value using binary search"
    low = 0
    high = len(search_list) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if search_list[mid] == value:
            return mid
        elif search_list[mid] > value:
            high = mid - 1
        else:
            low = mid + 1

    raise ValueError("value not in array")