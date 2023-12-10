print('''Welcome to Ena Minibus 
Route: Dhaka to chittagong
Time: 6:00 AM
Bus: Ac
Seat: 16
''')

seats = [["010", "Asif", "A1", "01790"], ["020", "Nasif", "A2", "01884"], ["030", "available", "A3", "number"],
         ["040", "available", "A4", "number"], ["050", "available", "B1", "number"],
         ["060", "available", "B2", "number"], ["070", "available", "B1", "number"],
         ["080", "available", "B4", "number"], ["090", "available", "C1", "number"],
         ["101", "available", "C2", "number"],
         ["111", "available", "C3", "number"], ["121", "available", "C4", "number"],
         ["131", "available", "D1", "number"], ["141", "available", "D2", "number"],
         ["151", "available", "D3", "number"],
         ["161", "available", "D4", "number"]]


def print_full_list():
    print("Seat status:")
    print("-----------------------------------")
    print("Seat no Passenger Ticket no")
    print("Ticket serial | Name       | Ticket no | Phone number | ")
    for i in range(0, len(seats)):
        print("{0:16}{1:15}{2:10}{3:1}".format(seats[i][0], seats[i][1], seats[i][2], seats[i][3]))
    print("\n")


def status_of_the_ticket():
    num = str(input("Enter the seat number: "))
    if num != 'available':
        for i in seats:
            if i[2] == num:
                t_info = i
                break
    if t_info == '':
        print("Ticket not found")
        print("\n")
    else:
        print("[Ticket serial|Name|Ticket no|Phone number]", "\n", i)
        print("\n")


def available_seats():
    for i in range(0, len(seats)):
        available_seats = []
        if seats[i][1] == 'available':
            available_seats.append(seats[i][2])
            print("Available seats: " + ', '.join(available_seats))


def ticket_booking():
    n = input("Which seat num do you want to booked? ")
    cancle_ticket = 0

    for i in range(len(seats)):
        for j in range(len(seats[i])):
            if seats[i][j] == n:
                index = i
                cancle_ticket = 1
    if  cancle_ticket == 1:
        ticket_ID = index
        if seats[ticket_ID][1] != "available":
            print("Seat All ready booked")
            print("\n")
        else:
            name = input("Enter your name: ")
            phone = input("Enter Your phone number:")
            seats[ticket_ID][1] = name
            seats[ticket_ID][3] = phone
            print("Your ticket Booked")
            print("Ticket serial | Name | Ticket no | Phone number | ")
            print("{0:16}{1:7}{2:12}{3}".format(seats[index][0], name, n, phone))
            print("\n")

    else:
        print('Ticket not found')



def cancle_ticket():
    st = str(input("Enter the ticket number serial number: "))
    cancle_ticket = 0
    if st != "available":
        for i in range(len(seats)):
            if seats[i][0] == st:
                seats[i] = [st, "available", seats[i][2], 'number']
                cancle_ticket = 1
                break
    if cancle_ticket == 1:
        print('Ticket cancelled')
        print("\n")
    else:
        print('Ticket not found')
        print("\n")


# Display the menu
print("")
print("What do you wish to do?")
print("1 -> All Seat status")
print("2 -> Only Available seats ")
print("3 -> Status of a single ticket")
print("4 -> Ticket booking")
print("5 -> Cancel a ticket")
print("0 -> Exit menu")
print("\n")  # For new line

option = 10  # Arbitrary value for entering while loop
while option != "0":  # Exit loop when the value is 0
    option = input("Select option: ")

    # Check chosen option and call the appropriate function
    if option == "1":
        # Call the print_full_list function
        print_full_list()
        print("\n")  # For new line
    elif option == "2":
        # Call the available_seats function
        available_seats()
        print("\n")  # For new line
    elif option == "3":
        # Call the status_of_the_ticket function
        status_of_the_ticket()
        print("\n")  # For new line
    elif option == "4":
        # Call the ticket_booking function
        ticket_booking()
        print("\n")  # For new line
    elif option == "5":
        # Call the cancle_ticket function
        cancle_ticket()
