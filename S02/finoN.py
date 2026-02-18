def fibon(n):
    n1 = 0
    n2 = 1

    if n == 0:
        result = n1
    elif n == 1:
        result = n2
    else:
        for i in range(2, n+1):
            a = n1 + n2
            n1 = n2
            n2 = a
        result = n2

    return result

print("5th Fibonacci term:", fibon(5))
print("10th Fibonacci term:", fibon(10))
print("15th Fibonacci term", fibon(15))
