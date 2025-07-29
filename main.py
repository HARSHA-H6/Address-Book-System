
from addressBook import AddressBook

print("Welcome to Address Book Program")
# Use Case 6 
address_book = dict()

while True:
    print("\n Choose Option: ")
    print("1. Add a new Address Book")
    print("2. Select an Address Book")
    print("3. Display all Address Books ")

    # Use case 7 and 8 are implemented to search by state and city
    print("4. Search By City ")
    print("5. Search By State ")
    print("6. Number of Contacts living in the same City ")
    print("7. Number of Contacts living in the same State")
    print("8. Sort entries in address book alphabetically by name ")
    # Use case 12 implemented to sort the address book using city, state or pin
    print("9. Sort the entries in Address Book using city, state or pincode")
    print("10. Exit")

    option_input = input("Enter Option: ")
    option = option_input.isdigit() and int(option_input) or None
    
    if option is None:
        print("Enter the Integer value: ")
        
    else:    
        match option:
            case 1:
                ab_name = input("Enter the name of the address book: ")
                if ab_name in address_book:
                    print("The book already exists! ")
                
                else:
                    address_book[ab_name] = AddressBook()
                    print(f"Address book with name {ab_name} is created.")
            
            case 2:
                name = input("Enter the name of the address book: ")
                
                if name not in address_book:
                    print(f"The Address book with the name {name} is not found! ")
                else:
                    select = address_book[name]
                    
                    while True: 
                        print(f"\n Address Book : {name}")
                        print("1. Add Contact")
                        print("2. Display Contacts")
                        print("3. Edit Contact")
                        print("4. Delete Contact")
                        print("5. Back to Address Book Menu")

                        choice = int(input("Choose option: "))

                        if choice == 1:
                            select.add_contacts()

                        elif choice == 2:
                            select.display_contacts()

                        elif choice == 3:
                            select.edit_contacts()
                        
                        elif choice == 4:
                            select.delete_contact()
                        
                        elif choice == 5:
                            break
                        else:
                            print("Invalid Option! ")
            
            case 3:
                if len(address_book) == 0:
                    print("No Address Book Found! ")
                else: 
                    for book in address_book:
                        print(book)
            
            case 4:
                res = []
                search = "city"
                city = input("Enter the name of the city to search: ")
                for book,abook in address_book.items():
                    for contact in abook.search_city_state(city,search):
                        res.append(contact)
                
                if len(res) !=0:
                    for contact in res:
                        print(contact)
                        print()
            
            case 5: 
                res = []
                search = "state"
                state = input("Enter the name of the state to search: ")
                for book,abook in address_book.items():
                    for contact in abook.search_city_state(state,search):
                        res.append(contact)

                if len(res) !=0:
                    for contact in res:
                        print(contact)
                        print()

            # Use Case 10: Feature to find the number of contact person in particular city
            case 6:
                res = []
                search = "city"
                city = input("Enter the name of the city to search: ")
                for book, abook in address_book.items():
                    for contact in abook.search_city_state(city, search):
                        res.append(contact)

                print(f"The number of contacts existing with the city name {city} are {len(res)}")

                if len(res) == 0:
                    print(f"No contacts found with the city name {city}")
            
            # Use Case 10: Feature to find the number of contact person in particular state
            case 7: 
                res = []
                search = "state"
                state = input("Enter the name of the state to search: ")
                for book,abook in address_book.items():
                    for contact in abook.search_city_state(state, search):
                        res.append(contact)
                print(f"The number of contacts existing with the state name{state} are {len(res)}")
                
                if len(res) == 0:
                    print(f"No contacts found with the state name {state}")

            # Usecase 11 sort the adddress book based on the name 
            case 8:
                name = input("Enter the name of the address book you want to sort: ")
                if name in address_book:
                    address_book[name].sort_contacts_by_name()
                else:
                    print(f"No address book found with name {name}")

            case 9:
                name = input("Enter the name of the address book you want to sort: ")
                if name in address_book:
                    select = address_book[name]
                    print("\n Sort by:")
                    print("1.City")
                    print("2.State")
                    print("3.Pin code")

                    choice = int(input("Enter the option: "))

                    if choice == 1:
                        select.sort_contacts_by_field("city")
                    elif choice ==2:
                        select.sort_contacts_by_field("state")
                    elif choice == 3:
                        select.sort_contacts_by_field("pin")
                    else:
                        print("Enter the valid option..")
                else:
                    print(f"No book found with the name {name}")

            case 10:
                print("Thank You ")
                break

            case _ :
                print("Invalid Option! ")


            