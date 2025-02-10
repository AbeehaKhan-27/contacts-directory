def display_people(people):
    for i, person in enumerate(people):
        print(i + 1, "-", person ["name"], "|", person ["age"], "|", person ["email"])

def add_person():
    for i in range(3):
        name = input("Name: ")
        age = input("Age: ")
        email = input("Email: ")

        person = {"name": name, "age": age, "email": email}
        return person
    
def delete_contact(people):
    display_people(people)

    while True:
        number = input("Enter a number to delete: ")
        try:
            number = int(number)
            if number <= 0 or number > len (people):
                print("Invalid number, out of range.")
            else:
                break
        except:
            print ("Invalid number")

    people.pop(number - 1)
    print("Person deleted.")

def search (people):
    search_name = input("Search for a name: ").lower ()
    results = []

    for person in people:
        name = person["name" ]
        if search_name in name.lower():
            results.append(person)

    display_people(results)