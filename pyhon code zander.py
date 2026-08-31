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