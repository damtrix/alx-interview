#!/usr/bin/python3

def factorial(n):
    if (n == 0):
        return 1
    else:
        return n * factorial(n - 1)

def pascal_triangle(n):
    
    if n <= 0:
        return []
    
    triangle = [0] * n
    for i in range(n):
        new_array = []
        for j in range(i+1):
            c = factorial(i) // (factorial(j) * factorial(i - j))
            new_array.append('{}'.format(c))
            
        triangle[i] = new_array
            
    return triangle