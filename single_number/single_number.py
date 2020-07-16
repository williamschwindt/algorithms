'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# O(n^2)
# def single_number(arr):
#     #loop over the array on keep track of the current int
#     for i in range(0, len(arr)):
#     #loop over again and compare that int to every other int
#         for j in range(0, len(arr)):
#     #if there is a duplicate pop off both ints
#             if arr[j] == arr[i] and i != j:
#                 arr[j] = ''
#                 arr[i] = ''
#     for i in arr:
#         if i != '':
#             return i


#O(n)
def single_number(arr):
    #create a cache
    count_cache = {}
    #loop over and insert the count of each number into the cache
    for num in arr:
        if num in count_cache:
            count_cache[num] += 1
        else:
            count_cache[num] = 1
    #loop over and return the number that has a count of 1
    for num in arr:
        if count_cache[num] == 1:
            return num



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")