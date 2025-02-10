import json
import utility

print("Hi, welcome to the Contacts Management System!")
print()


with open ("contacts.json", "r") as f:
    people = json.load(f)["contacts"]

while True:
    print("Contact list size:", len())
    command = input("You can 'Add', 'Delete', or 'Search' and 'Q' for quit: ").lower()

    if command == "add":
        person = utility.add_person()
        people.append(person)
        print("Person added!")
    elif command == "delete":
        utility.delete_contact(people)
    elif command == "search":
        utility.search(people)
    elif command == "q":
        break
    else:
        print("Invalid command.")

with open ("contacts.json", "w") as f:
    json.dump(f, {"contacts": people})