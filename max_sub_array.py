
def find_the_max_sum_of_subarray(arr, K):
    # Input: [2, 1, 5, 1, 3, 2], k=3 
    # Output: 9
    start_index = 0
    sum_index = 0
    target_sum = 0
    
    for index, value in enumerate(arr):
        sum_index += value
        if index >= K-1:
            if sum_index > target_sum:
                target_sum = sum_index
            sum_index -= arr[start_index]
            start_index +=1
    
    return target_sum



v = find_the_max_sum_of_subarray([2, 1, 20, 1, 3, 2], 3)
print(v)