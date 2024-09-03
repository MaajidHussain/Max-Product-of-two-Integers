def max_product(arr):
    # TODO
    if len(arr) <2:
        raise ValueError("Array Should contain minimum of 2 elemenrs to perform operation")
    unique_elements=list(set(arr))
    
    unique_elements.sort()
    
    firstMaxElement=unique_elements[-1]
    secondMaxElement=unique_elements[-2]
    
    
    operation=firstMaxElement * secondMaxElement
    return operation

array=[2,3,4,5,6,6,7,7,8,8]
print(max_product(array))
