class Patient: # Parent class that defines all the methods that will be inherited by the subclasses
    def __init__(self, patientname, patientbill_amount): # Initializes the attributes
        self.patientname = patientname # Name attribute
        self.patientbill_amount = patientbill_amount # Bill attribute

    def get_patientsname(self): # getter method for name (Returns the value)
        return self.patientname

    def get_billamount(self): # getter method for bill amount (Returns the value)
        return self.patientbill_amount
        
    def set_patientname(self, name2): # setter method for name (Replaces the current value)
        self.patientname = name2

    def set_billamount(self, billamount2): # setter method for bill amount (Replaces the current value)
        self.patientbill_amount = billamount2

    def calculate_bill(self): # returns the bill amount of a regualr patient that has no discounts
        return self.patientbill_amount


class Senior(Patient): # Child class that inherits the parent class "Patient"
    def __init__(self, patientname, patientbill_amount, discount): # Initializes the attributes
        super().__init__(patientname, patientbill_amount) # Calls the previous defined methods of the parent class to be used in the child class
        self.discount = discount # Discount attribute

    def calculate_bill(self): # returns the bill amount of a senior citizen with senior benefits
        discounted_amount = self.patientbill_amount * (1 - self.discount)
        return discounted_amount

    def display_type(self): # Displays the type of patient if they have benefits or not
        return "Senior Citizen"


class PhilHealth(Patient): # Child class that inherits the parent class "Patient"
    def __init__(self, patientname, patientbill_amount, philhealth_discount): # Initializes the attributes
        super().__init__(patientname, patientbill_amount) # Calls the previous defined methods of the parent class to be used in the child class
        self.philhealth_discount = philhealth_discount

    def calculate_bill(self): # returns the bill amount of a insurance holder of philhealth
        discounted_amount = self.patientbill_amount * (1 - self.philhealth_discount)
        return discounted_amount

    def display_type(self): # Displays the type of patient if they have benefits or not
        return "PhilHealth Member"


# The display of the actual program
patient = Patient("Juan Dela Cruz", 15000)
philhealth = PhilHealth("Maria Santos", 15000, 0.2)
senior = Senior("Pedro Reyes", 15000, 0.15)

print("Hospital Billing System")
print("------------------------")

print("Patient:", patient.get_patientsname())
print("Type: Regular Patient")
print("Bill Amount:", patient.get_billamount())
print("Final Bill:", patient.calculate_bill())

print("------------------------")

print("Patient:", philhealth.get_patientsname())
print("Type:", philhealth.display_type())
print("Bill Amount:", philhealth.get_billamount())
print("Final Bill:", philhealth.calculate_bill())

print("------------------------")

print("Patient:", senior.get_patientsname())
print("Type:", senior.display_type())
print("Bill Amount:", senior.get_billamount())
print("Final Bill:", senior.calculate_bill())

print("------------------------")

