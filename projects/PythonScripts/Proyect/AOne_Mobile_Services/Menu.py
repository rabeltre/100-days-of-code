
from PythonApplication2.AOne_Mobile_Services.DBConection import ContactDBApp
from PythonApplication2.AOne_Mobile_Services.Contact import Contact

contact = Contact()
contactdb = ContactDBApp()
option = None

while option != "7":
    print("\n**********Welcome to AOne Mobile Services**********\n")
    print("     App Menu    ")
    print("1 - Print list of contacts")
    print("2 - Add new contact")
    print("3 - Update existing contact")
    print("4 - Remove contact")
    print("5 - Search contact")
    print("6 - Call a contact")
    print("7 - Quit")
    option = input("Select the option: ")

    if option == "1":
        print("List of contacts")
        for row in contactdb.find_all_contact():
            print(f"Name: {row[0]}, Type of Contact={row[1]}, Phone number={row[2]}")
        option = input("Press any key to go the main menu. 7 - Quit: ")

    elif option == "2":
        print("Add new contact")
        contact.set_name(input("Name: "))
        if contactdb.check_if_contact_exist(contact):
            print("This contact name already exists")
        else:

            while True:
                print("Type of Contact:")
                print("1 - Personal")
                print("2 - Work")
                option = input("Must select one of the indicated options: ")
                if option == "1":
                    contact.set_type_of_contact("Personal")
                    break
                elif option == "2":
                    contact.set_type_of_contact("Work")
                    break

            contact.set_phone_call(input("Phone number: "))
            contactdb.add_contact(contact)
            print("Contact successfully added")

    elif option == "3":
        print("Update existing contact")
        contact.set_name(input("Name: "))
        if contactdb.check_if_contact_exist(contact):
            while True:
                print("Type of Contact:")
                print("1 - Personal")
                print("2 - Work")
                option = input("Must select one of the indicated options: ")
                if option == "1":
                    contact.set_type_of_contact("Personal")
                    break
                elif option == "2":
                    contact.set_type_of_contact("Work")
                    break

            contact.set_phone_call(input("Phone number: "))
            contactdb.update_contact(contact)
            print("Contact successfully modified")

        else:
            print("This contact name do not exists in the database")

    elif option == "4":
        print("Remove contact")
        contact.set_name(input("Name: "))
        if contactdb.check_if_contact_exist(contact):
            contactdb.delete_contact(contact)
            print(f"The contact name {contact.get_name()} has been removed.")
        else:
            print("This contact name do not exists in the database")

    elif option == "5":
        contact.set_name(input("Search name: "))
        if contactdb.check_if_contact_exist(contact):
            print("Info contact")
            for row in contactdb.find_contact_by_name(contact):
                print(f"Name: {row[0]}, Type of Contact={row[1]}, Phone number={row[2]}")
            option = input("Press any key to go the main menu. 7 - Quit: ")
        else:
            print("This contact name do not exists in the database")

    elif option == "6":
        contact.set_name(input("Search name: "))
        if contactdb.check_if_contact_exist(contact):
            print(f"Calling {contact.get_name()}....")

            option = input("Press any key to go the main menu. 7 - Quit: ")
        else:
            print("This contact name do not exists in the database")
            option = input("Press any key to go the main menu. 7 - Quit: ")





