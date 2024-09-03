def max_product(arr):
    # TODO
    if len(arr) <2:
        raise ValueError("Array Should contain minimum of 2 elemenrs to perform operation")
    max1=0
    max2=0
    
    for element in arr:
        if element>max1:
            max2=max1
            max1=element
            
        elif element>max2:
            max2=element
        
    return max1 * max2

array=[1, 7, 3, 4, 9, 5]
print(max_product(array))