import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-e1.json").read_text()

# Create the object person from the json string
person = json.loads(jsonstring)

people = person["people"]
print(f"Total people in the database: {len(people)}")

for i, person in enumerate(people):
    print()
    #termcolor.cprint("Person " + str(i + 1) + ": ", 'green')
    termcolor.cprint("Name: ", 'green', end='')
    print(person['Firstname'] + " " + person["Lastname"])
    termcolor.cprint("Age: ", 'green', end='')
    print(person['age'])

    # Get the phoneNumber list
    phoneNumbers = person['phoneNumber']

    # Print the number of elements in the list
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))

    # Print all the numbers
    for j, dictnum in enumerate(phoneNumbers):
        termcolor.cprint("  Phone " + str(j) + ": ", 'blue')

        # The element num contains 2 fields: number and type
        termcolor.cprint("\tType: ", 'red', end='')
        print(dictnum['type'])
        termcolor.cprint("\tNumber: ", 'red', end='')
        print(dictnum['number'])
