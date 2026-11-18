class Patient: # Parent class that defines all the methods that will be inherited by the subclasses
    def __init__(self, patientname, patientbill_amount): # Initializes
        self.patientname = patientname # Name attribute
        self.patientbill_amount = patientbill_amount # Bill attribute

    def get_patientsname(self):
        return self.patientname

    def get_billamount(self):
        return self.patientbill_amount
        
    def set_patientname(self, name2):
        self.patientname = name2

    def set_billamount(self, billamount2):
        self.bill_amount = billamount2

    def calculatebill(self):
        return self.patientbill_amount


class Senior(Patient):
    def __init__(self, patientname, patientbill_amount, discount):
        super().__init__(patientname, patientbill_amount)
        self.discount = discount

    def calculate_bill(self):
        discounted_amount = self.patientbill_amount * (1 - self.discount)
        return discounted_amount

    def display_patienttype(self):
        return "Senior Citizen"


class PhilHealth(Patient):
    def __init__(self, patientname, patientbill_amount, philhealth_discount):
        super().__init__(patientname, patientbill_amount)
        self.philhealth_discount = philhealth_discount

    def calculatebill(self):
        discounted_amount = self.patientbill_amount * (1 - self.philhealth_discount)
        return discounted_amount

    def displaypatienttype(self):
        return "PhilHealth Member"


patient = Patient("Juan Dela Cruz", 15000)
philhealth = PhilHealth("Maria Santos", 15000, 0.2)
senior = Senior("Pedro Reyes", 15000, 0.15)

print("Hospital Billing System")
print("------------------------")

print(f"Patient: {patient.getpatientsname()}")
print("Type: Regular Patient")
print(f"Bill Amount: {patient.getthebillamount():,.2f}")
print(f"Final Bill: {patient.calculatebill():,.2f}")

print()

print(f"Patient: {philhealth.getpatientsname()}")
print(f"Type: {philhealth.displaypatienttype()}")
print(f"Bill Amount: {philhealth.getthebillamount():,.2f}")
print(f"Final Bill: {philhealth.calculatebill():,.2f}")

print("------------------------")

print(f"Patient: {senior.getpatientsname()}")
print(f"Type: {senior.displaypatienttype()}")
print(f"Bill Amount: {senior.getthebillamount():,.2f}")
print(f"Final Bill: {senior.calculatebill():,.2f}")
