# Replace the "ANSWER HERE" for your answer

def sum_to_n(n):
    if n <= 0:
        return 0
    else:
        total = 0
        for i in range(1, n + 1):
            total += i
    return total

def sum_evens(n):
    if n <= 0:
        return 0
    total = 0
    for i in range (1, n + 1):
            if i % 2 == 0:
                total += i
    return total

def factorial(n):
    if n <= 0 :
        return 1
    fact = 1
    for i in range (n, 0, -1):
        fact *= i
    return fact
