#Exercise 6: Functions
#6a: Basic function
def is_even(n):
    if n % 2 == 0:
        result = "True"
    else:
        result = "False"
    return result

number = int(input("Enter a number: "))
print("is_even",number,"=",is_even(number))

#6b: Function with multiple parameters
def classify_triangle(a, b, c):
    if a == b == c:
        result = "equilateral"
    elif (a == b) or (a == c) or (b == c):
        result = "isosceles"
    else:
        result = "scalene"
    return result

print("classify_triangle(5, 5, 5) =", classify_triangle(5, 5, 5))
print("classify_triangle(3, 3, 4) =",classify_triangle(3, 3, 4))
print("classify_triangle(3, 4, 5) =",classify_triangle(3, 4, 5))

