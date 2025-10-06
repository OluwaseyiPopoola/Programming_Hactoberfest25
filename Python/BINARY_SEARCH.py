# Python's program to implement binary search
# Time Complexity: O(log N)
# Auxiliary Space: O(1)

def binary_search(nums: list[int], target: int) -> str|int:
    # Handles edge case when nums is empty
    if not nums:
        return "Cannot search an empty list"

    low, high = 0, len(nums) - 1
   
    # Keep iterating while there is still a possible subarray to be searche
    while low <= high:
        mid = (low + high) // 2

        # Check if value at mid equals target, then return position
        if nums[mid] == target:
            return mid
        
        # if value at mid < target, search target in right half
        elif nums[mid] < target:
            low = mid + 1

        # # if value at mid > target, search target in left half
        else:
            high = mid - 1
    
    return "target not found"

# Driver code:
def main():
    nums = [1, 3, 4, 5, 6, 7, 8]
    target = 6

if __name__ == "__main__":
    main()
