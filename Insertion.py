"""
MSCS532 Assignment 1: Insertion Sort Algorithm
Implementation of insertion sort for monotonically decreasing order

Roshan Acharya
7/5/2025
MSCS532 - Analysis of Algorithms
"""

def insertion_sort_decreasing(inputArray):
    """
    Sorts array inputArray in monotonically decreasing order using insertion sort.
    
    Args:
        inputArray: List of numbers to be sorted
    
    Returns:
        Sorted list in decreasing order
    """
    # Loop from second element to end
    for i in range(1, len(inputArray)):
        key = inputArray[i]
        j = i - 1
        
        # Move elements smaller than key one position ahead
        # Changed from inputArray[j] > key to inputArray[j] < key for decreasing order
        while j >= 0 and inputArray[j] < key:
            inputArray[j + 1] = inputArray[j]
            j = j - 1
        
        inputArray[j + 1] = key
    
    return inputArray


# Test the algorithm
if __name__ == "__main__":
    # Test array from the textbook example
    test_array = [5, 2, 4, 6, 1, 3]
    print("Original array:", test_array)
    
    # Sort in decreasing order
    sorted_array = insertion_sort_decreasing(test_array.copy())
    print("Sorted array (decreasing):", sorted_array)
    
    # Additional test cases
    test_cases = [
        [31, 41, 59, 26, 41, 58],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1]
    ]
    
    for i, arr in enumerate(test_cases, 1):
        print(f"\nTest {i}: {arr}")
        print(f"Sorted: {insertion_sort_decreasing(arr.copy())}")