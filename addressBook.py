
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