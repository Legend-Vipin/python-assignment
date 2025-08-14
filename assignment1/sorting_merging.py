def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

def merge_lists(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge_lists(left, right)

def higher_order_sort(lst, compare_func):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if compare_func(lst[j], lst[j+1]) > 0:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

# Example usage
if __name__ == "__main__":
    data = [64, 25, 12, 22, 11]

    print("Selection Sort:")
    print(selection_sort(data.copy()))

    print("\nMerge Sort:")
    print(merge_sort(data.copy()))

    print("\nHigher Order Sort (descending):")
    desc_compare = lambda x, y: y - x
    print(higher_order_sort(data.copy(), desc_compare))
