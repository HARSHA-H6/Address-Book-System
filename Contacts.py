class Contacts:
    """
    Step1: Create a class Contacts that accepts
    First Name, Last Name, Address, City and Contact Detatils
    """
    def __init__(self,firstname,lastname, address, city, state, pin, phoneno, email):
        
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.city = city
        self.state = state
        self.pin = pin
        self.phoneno = phoneno
        self.email = email

        # Step2: define the __str__ so that the when we print the object it prints the details of the person
    def __str__(self):
            return (f"Name: {self.firstname} {self.lastname}\n"
                    f"Address: {self.address} {self.city} {self.state} {self.pin}\n"
                    f"Phone Number:{self.phoneno} \nEmail:{self.email}")