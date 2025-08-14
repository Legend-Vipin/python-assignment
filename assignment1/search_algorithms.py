import time

def simple_search(lst, target):
    for i, item in enumerate(lst):
        if item == target:
            return i
    return -1

def binary_search(lst, target):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def estimate_search_time(search_func, lst, target, iterations=1000):
    start = time.time()
    for _ in range(iterations):
        search_func(lst, target)
    end = time.time()
    avg_time = (end - start) / iterations
    return avg_time

# Example usage
if __name__ == "__main__":
    data = list(range(1, 10001))
    target = 9999

    print("Simple Search:")
    index = simple_search(data, target)
    print(f"Found target at index: {index}")

    print("\nBinary Search:")
    index = binary_search(data, target)
    print(f"Found target at index: {index}")

    print("\nEstimating Search Times:")
    simple_time = estimate_search_time(simple_search, data, target)
    binary_time = estimate_search_time(binary_search, data, target)
    print(f"Average time for simple search: {simple_time:.10f} seconds")
    print(f"Average time for binary search: {binary_time:.10f} seconds")
