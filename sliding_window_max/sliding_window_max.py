'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

from binary_search_tree import BSTNode
from collections import deque

# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# will have to calculate max ((length - K) + 1) times

# def sliding_window_max(nums, k): 
#     max_list = []
#     #track start and end
#     start = 0
#     end = k - 1
#     #loop through ((length - K) + 1) times
#     for i in range(0, (len(nums) - k) + 1):
#         window = nums[start:end + 1]
#         #calculate max
#         max_int = max(window)
#         max_list.append(max_int)
#         #update start and end
#         start += 1
#         end += 1
#     return max_list

# def sliding_window_max(nums, k):
#     max_list = []
#     #track start and end
#     start = 0
#     end = k - 1

#     #find the first window and first max
#     first_window = nums[start:end + 1]
#     curr_max = max(first_window)

#     #loop through ((length - K) + 1) times
#     for i in range(0, (len(nums) - k) + 1):
#         #find the window
#         window = nums[start:end + 1]

#         #if the curr_max is in the window compare to the newe el in the window
#         if nums.index(curr_max) >= start and nums.index(curr_max) <= end:
#             #if the new el is larger set curr_max 
#             if window[-1] > curr_max:
#                 curr_max = window[-1]
#         #if the curr_max isn't in the window recalculate the max with the whole window
#         else:
#             curr_max = max(window)

#         #append curr_max to max_list
#         max_list.append(curr_max)

#         #update start and end
#         start += 1
#         end += 1
#     return max_list


# def sliding_window_max(nums, k):
#     max_list = []
#     start = 1
#     end = k -1

#     #helper function to create a bst with the nums in the window and find the max
#     def get_max(start_point, end_point):
#         #initialize bst with first el
#         bst = BSTNode(nums[start_point])
#         #loop through window and insert into bst
#         for i in range(start_point + 1, end_point + 1):
#             bst.insert(nums[i])
        
#         #find max 
#         max_list.append(bst.get_max())

#     #loop until window has reached end of list
#     for i in range(0, (len(nums) - k) + 1):
#         get_max(start - 1, end)
#         start += 1
#         end += 1

#     return max_list




def sliding_window_max(nums, k):
    de = deque()
    max_list = []

    for i in range(k):
        while de and nums[i] >= nums[de[-1]]:
            de.pop()
        de.append(i)

    for i in range(k, len(nums)):
        max_list.append(nums[de[0]])
          
        # Remove the elements which are  
        # out of this window 
        while de and de[0] <= i-k: 
              
            # remove from front of de 
            de.popleft()  
          
        # Remove all elements smaller than 
        # the currently being added element  
        # (Remove useless elements) 
        while de and nums[i] >= nums[de[-1]] : 
            de.pop() 
          
        # Add current element at the rear of de 
        de.append(i) 
      
    # Print the maximum element of last window 
    max_list.append(nums[de[0]])
    return max_list



    
if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
