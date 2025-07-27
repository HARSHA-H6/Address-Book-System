
# Step1: importing the Contacts.py 
from Contacts import Contacts

# Step2: creating the AddressBook class
class AddressBook:

    def __init__(self):
        self.contacts_list=[]
    
    # Step3: assigning the value to the variable
    def add_contacts(self):
        
        self.firstname = input("Enter first Name: ")
        self.lastname = input("Enter last Name: ")
        self.address = input("Enter the address: ")
        self.city = input("Enter the city: ")
        self.state = input("Enter the state: ")
        self.pin = input("Enter the pin: ")
        self.phoneno = input("Enter the phone number: ")
        self.email = input("Enter the email: ")

        # Step4: Create the object of the Contacts 
        new_contact  = Contacts(self.firstname,self.lastname,self.address,self.city,
                                self.state,self.pin,self.phoneno,self.email)
        
        self.contacts_list.append(new_contact)
    
    # Step6: Creating the function to display the contacts details
    def display_contacts(self):
        if len(self.contacts_list)==0:
            print("No contacts available")

        #Step7: Iterating the list        
        else:
            for contact in self.contacts_list:
                print(contact)
                print()

    # Create the findContact function
    def find_contacts(self,first_name, last_name):
        for contact in self.contacts_list:
            if contact.firstname == first_name and contact.lastname == last_name:
                return contact
            
            else:
                return None
            
    # Use Case 3 added the EditContact function

    def edit_contacts(self):
        
        first_name = input("Enter the first name of the contact: ")
        last_name = input("Enter the second name of the contact: ")

        contact = self.find_contacts(first_name, last_name)

        if contact is None:
            print("No contact is found")
        else:
            print("Contact found! ")
            print("\n Select the field you want to edit ")
            print("1.Address")
            print("2.City")
            print("3.State")
            print("4.Pin code")
            print("5.Phone Number")
            print("6.Email Id")

            option_input = input("Enter the option: ")
            
            option = option_input.isdigit() and int(option_input) or None

            if option is None:
                print("You have entered the invalid option\n Enter the digit between 1 to 6")
            
            else:
                match option:
                    case 1: contact.address = input("Enter the new address: ")
                    case 2: contact.city = input("Enter the new city: ")
                    case 3: contact.state = input("Enter the new state: ")
                    case 4: contact.pin = input("Enter the new pin: ")
                    case 5: contact.phoneno = input("Enter the new phoneno: ") 
                    case 6: contact.email = input("Enter the new email: ") 

                    case _ : print("Invalid choice \n Enter the valid option")
    
    # Use Case 4 delete feature is updated
    def delete_contact(self):
        
        first_name = input("Enter the first name of the contact: ")
        last_name = input("Enter the last name of the contact: ")

        contact = self.find_contacts(first_name, last_name)

        if contact is None:
            print("Contact is not found!")
        
        else:
            print("Contact Found")
            for _ in self.contacts_list:
                if contact in self.contacts_list:
                    self.contacts_list.remove(contact)
                    print("Contact is Deleted! ")
