'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    #keep track of the products
    new_arr = []
    #loop through array
    for i in range(0, len(arr)):
        #reset the product after every outside loop iteration
        product = -1
        #loop through again
        for j in range(0, len(arr)):
            #calculate product
            product = product * arr[j] 
        #divide the total product by arr[i] and * -1 
        new_arr.append((product * -1) / arr[i])

    return new_arr

arr = [1, 2, 3, 4, 5]
print(product_of_all_other_numbers(arr))

    


# if __name__ == '__main__':
#     # Use the main function to test your implementation
#     # arr = [1, 2, 3, 4, 5]
#     arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

#     print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
