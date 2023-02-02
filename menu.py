import create
import read
import update
import delete


# create a function
def menuOptions():
    options = 0  # flag variable
    # while 0 not in this list ["1","2","3","4","5"]:
    while options not in ["1", "2", "3", "4", "5"]:
        print(
            "Film Menu Options\nEnter:\n1. To Print.\n2. To Add.\n3. To Update.\n4. To Delete.\n5. To Exit"
        )
        # re-assign the value for options variable
        # the default datatype for input is string
        options = input("Enter an option from the menu above: ")
        print(type(options))
        print(options)
        if options not in ["1", "2", "3", "4", "5"]:
            print(f"{options} is not a valid choice")
    return options


mainProgram = True  # assign the mainProgram a value with a boolean datatype of True
while mainProgram:  # same as while True
    mainMenu = menuOptions()
    if mainMenu == "1":
        read.readFilms()
    elif mainMenu == "2":
        create.insertFilms()
    elif mainMenu == "3":
        update.updateFilms()
    elif mainMenu == "4":
        delete.deleteFilms()
    else:  # re-assign the mainProgram a value with a boolean datatype of False
        mainProgram = False
input("Press enter to quit/exit the application")

"""
# Create Options menu
def show_menu():
    print("Options menu")
    print("1. Add a record")
    print("2. Delete a record")
    print("3. Amend a record")
    print("4. Print all records")
    print("5. Exit")
    option = int(input("Enter option number: "))
    return option

# Run the program
while True:
    option = show_menu()
    if option == 1:
        add_record()
    elif option == 2:
        delete_record()
    elif option == 3:
        amend_record()
    elif option == 4:
        print_records()
    elif option == 5:
        exit_program()
    else:
        print("Invalid option")

"""
