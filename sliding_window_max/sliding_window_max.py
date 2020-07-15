'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# will have to calculate max ((length - K) + 1) times

def sliding_window_max(nums, k):
    max_list = []
    #track start and end
    start = 0
    end = k - 1
    #loop through ((length - K) + 1) times
    for i in range(0, (len(nums) - k) + 1):
        window = nums[start:end + 1]
        #calculate max
        max_int = max(window)
        max_list.append(max_int)
        #update start and end
        start += 1
        end += 1
    return max_list

# arr1 = [1,3,-1,-3,5,3,6,7]
# print(sliding_window_max(arr1, 3))


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
