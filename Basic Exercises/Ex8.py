#Exercise 8: Combining everything

students = [
    {"name": "Ana", "grades": [8.5, 7.0, 9.0]},
    {"name": "Luis", "grades": [5.0, 4.5, 6.0]},
    {"name": "Maria", "grades": [9.5, 9.0, 10.0]},
    {"name": "Pedro", "grades": [3.0, 4.0, 2.5]},
    {"name": "Sofia", "grades": [7.0, 7.5, 8.0]},
]

def average(grades):
    tot = 0
    for i in range(len(grades)):
        tot += grades [i]
    return round(tot/len(grades), 1)

def get_status(avg):
    if avg >= 5:
        result = "PASS"
    else:
        result = "FAIL"
    return result


count_pass = 0
count_fail = 0

for student in students:
    avg = average(student["grades"])
    status = get_status(avg)
    print(student["name"],":",avg,"->",status)

    if status == "PASS":
        count_pass += 1
    else:
        count_fail += 1
print("Results:", count_pass,"passed,",count_fail,"failed")
