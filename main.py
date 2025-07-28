
from addressBook import AddressBook

print("Welcome to Address Book Program")

address_book = dict()

while True:
    print("\n Choose Option: ")
    print("1. Add a new Address Book")
    print("2. Select an Address Book")
    print("3. Display all Address Books ")
    print("4. Exit")

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
                print("Thank You ")
                break

            case _ :
                print("Invalid Option! ")


            