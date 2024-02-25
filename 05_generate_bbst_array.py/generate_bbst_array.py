"""
Generate BBST (Balanced Binary Search Tree) Array
"""

def GenerateBBSTArray(a):
    a = a[:]
    a.sort()
    step = len(a)
    result_array = []
    return GenerateBBSTArray_recursion(a, step, result_array)

def GenerateBBSTArray_recursion(a, step, result_array):
    indentation_of_first_element = (step - 1) // 2
    for element_id in range(indentation_of_first_element, len(a), step):
        result_array.append(a[element_id])
    if indentation_of_first_element == 0:
        return result_array
    next_step = (step + 1) // 2
    return GenerateBBSTArray_recursion(a, next_step, result_array)

