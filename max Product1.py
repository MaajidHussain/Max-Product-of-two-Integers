def max_product(arr):
    # TODO
    if len(arr) <2:
        raise ValueError("Array Should contain minimum of 2 elemenrs to perform operation")
    first_max_element=max(arr)
    
    sortings=arr.sort()
    
    second_max_element=arr[-2]
    
    operation=first_max_element * second_max_element
    return operation

array=[1,7,3,4,9,5]
print(max_product(array))
