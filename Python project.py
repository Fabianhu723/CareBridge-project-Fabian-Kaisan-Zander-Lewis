def assign_triage_room():
    while True:
        try:
            severity = int(input("Enter severity condition (1 to 10): "))

            if severity < 1 or severity > 10:
                print("Invalid input, please enter a whole number from 1 to 10.")
                continue

            break

        except ValueError:
            print("Invalid input, please enter a whole number from 1 to 10.")

    if 1 <= severity <= 4:
        room = "Waiting Room"
    elif 5 <= severity <= 7:
        room = "Room 1"
    else:
        room = "Room 2"

    print("\nTriage Summary")
    print("Severity Level:", severity)
    print("Assigned Room:", room)


assign_triage_room()