from PhoneBookFunctions import *

while True:
    print("---------------------------")
    print("Select a function:")
    print("1. Add contact", "2. Delete contact", "3. Show contact list", "4. Change number", "5. Exit", sep='\n')
    print("---------------------------")
    function = int(input("Enter the function number: "))
    if function == 1:
        add(input("Enter the contact name: "), input("Enter the phone number: "))
        print("The contact has been successfully added")
    elif function == 2:
        delete(input("Enter the contact name: "))
    elif function == 3:
        print("Contact list: ")
        check()
    elif function == 4:
        change(input("Enter the contact name: "))
        print("The contact has been successfully changed")
    else:
        exit(0)
