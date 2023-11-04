#Task 2

#Extend Phonebook application

#Functionality of Phonebook application:

#Add new entries 
#Search by first name 
#Search by last name 
#Search by full name
#Search by telephone number
#Search by city or state
#Delete a record for a given telephone number
#Update a record for a given telephone number
#An option to exit the program
 

#The first argument to the application should be the name of the phonebook. Application should load JSON data, if it is present in the folder with application, else raise an error. After the user exits, all data should be saved to loaded JSON.





import json
import os


def load_phonebook(filename):
    if os.path.isfile(filename):
        with open(filename, 'r') as file:
            phonebook_data = json.load(file)
        return phonebook_data
    else:
        return []


def save_phonebook(filename, phonebook_data):
    with open(filename, 'w') as file:
        json.dump(phonebook_data, file, indent=4)


def add_entry(phonebook_data, first_name, last_name, telephone, city, state):
    entry = {
        "first_name": first_name,
        "last_name": last_name,
        "telephone": telephone,
        "city": city,
        "state": state,
    }
    phonebook_data.append(entry)
    print("Entry added successfully.")


def search_entries(phonebook_data, criteria, value):
    results = []
    for entry in phonebook_data:
        if entry[criteria].lower() == value.lower():
            results.append(entry)
    return results


def delete_entry(phonebook_data, telephone):
    for entry in phonebook_data:
        if entry["telephone"] == telephone:
            phonebook_data.remove(entry)
            print("Entry deleted successfully.")
            return
    print("Entry not found with the provided telephone number.")


def update_entry(phonebook_data, telephone, new_data):
    for entry in phonebook_data:
        if entry["telephone"] == telephone:
            entry.update(new_data)
            print("Entry updated successfully.")
            return
    print("Entry not found with the provided telephone number.")


def main():
    phonebook_filename = "phonebook.json"
    phonebook_data = load_phonebook(phonebook_filename)

    while True:
        print("\nPhonebook Application")
        print("1. Add new entry")
        print("2. Search by first name")
        print("3. Search by last name")
        print("4. Search by full name")
        print("5. Search by telephone number")
        print("6. Search by city or state")
        print("7. Delete a record by telephone number")
        print("8. Update a record by telephone number")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            telephone = input("Enter telephone number: ")
            city = input("Enter city: ")
            state = input("Enter state: ")
            add_entry(phonebook_data, first_name, last_name, telephone, city, state)
        elif choice == '2':
            first_name = input("Enter first name to search: ")
            results = search_entries(phonebook_data, "first_name", first_name)
            for entry in results:
                print(entry)
        elif choice == '3':
            last_name = input("Enter last name to search: ")
            results = search_entries(phonebook_data, "last_name", last_name)
            for entry in results:
                print(entry)
        elif choice == '4':
            full_name = input("Enter full name to search: ")
            for entry in phonebook_data:
                if full_name.lower() in (entry["first_name"] + " " + entry["last_name"]).lower():
                    print(entry)
        elif choice == '5':
            telephone = input("Enter telephone number to search: ")
            results = search_entries(phonebook_data, "telephone", telephone)
            for entry in results:
                print(entry)
        elif choice == '6':
            city_or_state = input("Enter city or state to search: ")
            results = search_entries(phonebook_data, "city", city_or_state) + search_entries(phonebook_data, "state", city_or_state)
            for entry in results:
                print(entry)
        elif choice == '7':
            telephone = input("Enter telephone number to delete: ")
            delete_entry(phonebook_data, telephone)
        elif choice == '8':
            telephone = input("Enter telephone number to update: ")
            new_data = {
                "first_name": input("Enter new first name: "),
                "last_name": input("Enter new last name: "),
                "telephone": input("Enter new telephone number: "),
                "city": input("Enter new city: "),
                "state": input("Enter new state: "),
            }
            update_entry(phonebook_data, telephone, new_data)
        elif choice == '9':
            save_phonebook(phonebook_filename, phonebook_data)
            print("Phonebook data saved. Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
