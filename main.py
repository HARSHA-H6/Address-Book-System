
from addressBook import AddressBook
# Step1: Print the welcome statement 

print("Welcome to Address Book Program")

# Step2: Creating the object of the AddressBook()
address_book = AddressBook()

# Step3: Creating the switch statement using the below logic
while True:
    print(f"Choose Options",
          f"1.Add Contact",
          f"2.Display Contacts",
          f"3.Exit")
    
    option = int(input("Enter the option: "))
    
    if option == 1:
        #Step4: calling the add_contacts() functions in the AddressBook
        address_book.add_contacts()

    elif option == 2:
        # Step5: Calling the display_contacts() functions in the AddressBook
        address_book.display_contacts()
    
    else:
        # Step6: Option to Exit the while loop
        print("Thank you")
        break