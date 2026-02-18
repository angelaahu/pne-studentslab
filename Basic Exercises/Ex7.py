#Exercise 7: Dictionaries
student = {
    "name": "Carlos",
    "age": 22,
    "subjects": ["PNE", "Networks", "Databases"],
    "grades": {"PNE": 8.5, "Networks": 7.0, "Databases": 9.2}
}

print("Name:", student["name"])
print("Number of subjects:", len(student["subjects"]))

if "PNE" in student["subjects"]:
    print("Enrolled in PNE: True")
else:
    print("Enrolled in PNE: False")

print("Databases grade:", student["grades"]["Databases"])

total = 0
for grade in student["grades"].values():
    total += grade
average = round(total/len(student["grades"]),2)
print("Average grade:", average)

print("Subject grades: ")
for key, value in student["grades"].items():
    print(f'{key}: {value}')





