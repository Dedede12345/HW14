def sum_n(n):
    '''Returns sum of all n preceding numbers'''
    if n == 0:
        return 0
    else:
        return n + sum_n(n - 1)

# print(sum_n(9))

def factorial(n):
    '''Returns factorial of a n number'''
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# print(factorial(5))

def fibonachi(n):
    '''Returns Fibonachi Number at nth position'''
    if n == 0: return 0
    if n == 1: return 1
    else:
        return fibonachi(n - 1) + fibonachi(n - 2)

# print(fibonachi(9))

