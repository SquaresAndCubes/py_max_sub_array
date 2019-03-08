"""
Brent Vaalburg
CSCI445
Week 1 Divide and Conquer Algorithm - Max Sub Array
Code Modeled from Reference:
Python Program to solve Maximum Subarray Problem using Divide and Conquer - Sanfoundry. (2019).
Retrieved from https://www.sanfoundry.com/python-program-solve-maximum-subarray-problem-using-divide-conquer/
"""

def max_subarray(lista, start, end):

    if start == end - 1:
        return start, end, lista[start]
    else:
        middle = (start + end) // 2
        ls, le, lmax = max_subarray(lista, start, middle)
        rs, re, rmax = max_subarray(lista, middle, end)
        xstart, xend, xmax = max_crossing_subarray(lista, start, middle, end)
        if (lmax > rmax and lmax > xmax):
            return ls, le, lmax
        elif (rmax > lmax and rmax > xmax):
            return rs, re, rmax
        else:
            return xstart, xend, xmax


def max_crossing_subarray(lista, start, middle, end):

    left_sum = float('-inf')
    temp_sum = 0
    x_start = middle
    for i in range(middle - 1, start - 1, -1):
        temp_sum = temp_sum + lista[i]
        if temp_sum > left_sum:
            left_sum = temp_sum
            x_start = i

    right_sum = float('-inf')
    temp_sum = 0
    x_end = middle + 1
    for i in range(middle, end):
        temp_sum = temp_sum + lista[i]
        if temp_sum > right_sum:
            right_sum = temp_sum
            x_end = i + 1
    return x_start, x_end, left_sum + right_sum


lista = input('Enter array of numbers separated by commas: ')
lista = lista.split(',')
lista = [int(x) for x in lista]
start, end, maximum = max_subarray(lista, 0, len(lista))

print('The max subarray begins at index {} and ends at index {}'
      ' and has a total of {}.'.format(start, end - 1, maximum))
