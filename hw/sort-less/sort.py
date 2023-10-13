import time


def read_data(filename) -> list[int]:
    """
    Read data from a text file and return a list of integers.

    Args:
        filename (str): The name of the text file to read data from.

    Returns:
        list[int]: A list of integers read from the file.
    """
    with open(filename, 'r') as f:
        data = f.readlines()

    nums = []
    for line in data:
        nums.append(int(line.strip()))
    return nums


def selection_sort(arr):
    """
    Sort a list using the selection sort algorithm.
    """
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]


def time_selection_sort(nums):
    """
    Measure the running time of the selection sort algorithm on a list of integers.
    """
    start_time = time.time()
    selection_sort(nums)
    end_time = time.time()
    print(f"Selction Sorting running time: {end_time - start_time}s")


def bubble_sort(arr):
    """
    Sort a list using the bubble sort algorithm.
    """
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        swapped = False  # Used to flag if any swap occurred in this pass

        # Last i elements are already in place, so we don't need to compare them again
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            # If no swaps occurred in a pass, the list is already sorted, so we can stop
            break


def time_bubble_sort(nums):
    """
    Measure the running time of the bubble sort algorithm on a list of integers.
    """
    start_time = time.time()
    bubble_sort(nums)
    end_time = time.time()
    print(f"Bubble Sorting running time: {end_time - start_time}s")


def merge(left, right):
    """
    Merges two sorted lists into a single sorted list
    """
    result, left_idx, right_idx = [], 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result


def merge_sort(arr):
    """
    Sort a list using the merge sort algorithm.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left, right = arr[:mid], arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def time_merge_sort(nums):
    """
    Measure the running time of the merge sort algorithm on a list of integers.
    """
    start_time = time.time()
    merge_sort(nums)
    end_time = time.time()
    print(f"Merge Sorting running time: {end_time - start_time}s")


def compare_sorting_algorithms():
    """
    Compare the performance of different sorting algorithms on different datasets
    """
    random_files = ['random5000.txt', 'random10000.txt', 'random50000.txt']

    for file in random_files:
        print(f'Now sorting {file}:')
        data = read_data(f'data/{file}')
        time_selection_sort(data[:])
        time_bubble_sort(data[:])
        time_merge_sort(data[:])
        print()

    sorted_files = ['sorted5000.txt', 'sorted10000.txt', 'sorted50000.txt']

    for file in sorted_files:
        print(f'Now sorting {file}:')
        data = read_data(f'data/{file}')
        time_selection_sort(data[:])
        time_bubble_sort(data[:])
        time_merge_sort(data[:])
        print()

    reversed_files = ['reversed5000.txt', 'reversed10000.txt', 'reversed50000.txt']

    for file in reversed_files:
        print(f'Now sorting {file}:')
        data = read_data(f'data/{file}')
        time_selection_sort(data[:])
        time_bubble_sort(data[:])
        time_merge_sort(data[:])
        print()


def main():
    """"""
    compare_sorting_algorithms()


if __name__ == '__main__':
    main()
