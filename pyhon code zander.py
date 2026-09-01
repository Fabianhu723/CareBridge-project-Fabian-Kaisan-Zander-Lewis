# Enter patient name
name = input("Enter patient name: ")

while name == "":
    print("Invalid name")
    name = input("Enter patient name again: ")

# Enter patient age
age = input("Enter patient age: ")

while not age.isdigit() or int(age) <= 0:
    print("Invalid age")
    age = input("Enter patient age again: ")

age = int(age)

# Enter patient ID
patientID = input("Enter patient ID: ")

while patientID == "":
    print("Invalid ID")
    patientID = input("Enter patient ID again: ")

# Display patient details
print("Patient name:", name)
print("Patient age:", age)

print("Patient ID:", patientID)
print("Patient added successfully")
while True:
    # Ask the user for the department and date
    department = input("Choose department (GP or Specialist): ")
    date = input("Enter date: ")

    # Check if the department or date is invalid
    if department not in ["GP", "Specialist"] or date == "":
        print("Error: Invalid department or date.")
        print("Please choose the department and date again.")

    else:
        # Ask the user to confirm the purchase
        print("Do you wish to confirm the purchase?")
        confirmation = input("Enter Yes or No: ")

        if confirmation == "Yes":
            print("Purchase confirmed.")
            break
BASE_FEE = 100
LAB_TEST_RATE = 10

patientType = input("Enter patient type (Subsidised / Private): ")

while patientType not in ("Subsidised", "Private"):
    print("Invalid patient type")
    patientType = input("Enter patient type again: ")

while True:
    try:
        labTests = int(input("Enter number of lab tests completed: "))
        break
    except ValueError:
        print("Invalid number of lab tests")

subtotal = BASE_FEE + (labTests * LAB_TEST_RATE)

if patientType == "Subsidised":
    total = subtotal * 0.70
else:
    total = subtotal

print("Patient type:", patientType)
print("Total amount to pay: $", format(total, ".2f"))
