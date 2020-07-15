'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # #keep track of the indexes of the zeros
    # indexes = []
    # returned_arr = []
    # #loop through
    # for i in range(0, len(arr)):
    # #if the curr num is 0 append 0 to the end
    #     if arr[i] == 0:
    #         arr.append(0)
    #         #add index to array
    #         indexes.append(i)

    # for index in indexes:
    #     arr[index] = ''

    # for i in arr:
    #     if i is not '':
    #         returned_arr.append(i)

    # return returned_arr

    for i in range(0,len(arr)):
        if arr[i] == 0:
            arr.remove(arr[i])
            arr.append(0)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")