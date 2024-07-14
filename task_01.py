
import timeit
import random
import matplotlib.pyplot as plt

import sys

# Increase the recursion limit
sys.setrecursionlimit(50000)

# Generate test data
def generate_random_list(size):
    return list(random.randint(1, 1000) for _ in range(size))

# Merge sort
def merge(left, right):
    result = [] 
    left_index, right_index = 0, 0 

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result  

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)  


# Insertion Sort
def insertion_sort(arr, n):
    if n <= 1:  
        return

    insertion_sort(arr, n - 1)  

    key = arr[n - 1]  
    j = n - 2  
    while j >= 0 and arr[j] > key:  
        arr[j + 1] = arr[j]  
        j -= 1  
    arr[j + 1] = key  
    return arr  


# Method sorted()
def sorted_method(arr):
    result = sorted(arr)
    return result


# Method sort()
def sort_method(arr):
    result = arr.sort()
    return result

def measure_time(sort_function, array):
    start = timeit.default_timer()
    if sort_function == insertion_sort:
        sort_function(array, len(array))
    else:
        sort_function(array)
    
    return timeit.default_timer() - start


if __name__ == "__main__":
    sizes = [100, 500, 100, 5000, 10000]
    #sizes = [10, 50, 100]
    algorithms = [merge_sort, insertion_sort, sorted_method, sort_method]
    results = {alg.__name__: [] for alg in algorithms}

    for s in sizes:
        array = generate_random_list(s)
        
        for alg in algorithms:
            arr = array.copy()
            try:
                time = measure_time(alg, arr)
                results[alg.__name__].append(time)
                print(f"{alg.__name__} for {s} elements time: {time:.5f}")
            except RecursionError:
                print(f"{alg.__name__} for {s} elements: RecursionError")
        print(results)
 
# Visualyzing results:
for alg in algorithms:
    plt.plot(sizes, results[alg.__name__], label=alg.__name__)

plt.xlabel('Lenth of the array')
plt.ylabel('Processing time (sec)')
plt.legend()
plt.show()


"""
 Висновок:
 Складність вбудованих функцій сотрування О(1)

"""