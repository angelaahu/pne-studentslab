#Exercise 4: Conditionals
def calc_score(score):
    if 9 <= score <= 10:
        result = "A"
    elif 7 <= score <= 8.9:
        result = "B"
    elif 5 <= score <= 6.9:
        result = "C"
    elif 3 <= score <= 4.9:
        result = "D"
    elif 0 <= score <= 2.9:
        result = "F"
    else:
        result = "Not valid"
    return result

score = float(input("Enter your grade: "))
print("Score:", score, "->", calc_score(score))