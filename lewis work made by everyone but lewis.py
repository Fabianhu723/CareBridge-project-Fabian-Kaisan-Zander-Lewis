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
