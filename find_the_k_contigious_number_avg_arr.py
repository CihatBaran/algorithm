print("something!")


def find_the_avg_for_contigious_subarray(arr, K):
    """
        Sliding window...
    """
    window_start = 0
    window_sum = 0
    avg = []

    for k in range(len(arr)):
        window_sum += arr[k]

        if k >= (K-1):
            avg.append(window_sum / K)
            window_sum -= arr[window_start]
            window_start += 1
    print(avg)


find_the_avg_for_contigious_subarray(
    [0	,1	,2	,3	,4	,5	,6	,7	,8	,9], 5
    )