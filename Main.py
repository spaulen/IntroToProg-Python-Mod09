# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# SPaulen, 12.14.2020,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
# Done: Import Modules
import IOClasses as I
import ProcessingClasses as P
import DataClasses as D

# Declare Variables
strFileName = "EmployeeData.txt"

# Main Body of Script  ---------------------------------------------------- #
# Done: Add Data Code to the Main body

# Load data from file into a list of employee objects when script starts
lstEmployeeData = P.FileProcessor.read_data_from_file(strFileName)

# Show user a menu of options
while True:
    try:
        # Get user's menu option choice
        I.EmployeeIO.print_menu_items()
        strChoice = I.EmployeeIO.input_menu_options()
        # Show user current data in the list of employee objects
        if strChoice.strip() == "1":
            I.EmployeeIO.print_current_list_items(lstEmployeeData)
            continue
        # Let user add data to the list of employee objects
        elif strChoice == "2":
            lstEmployeeData.append(I.EmployeeIO.input_employee_data())
            continue
        # let user save current data to file
        elif strChoice == "3":
            strStatus = P.FileProcessor.save_data_to_file(strFileName, lstEmployeeData)
            continue
        # Let user exit program
        elif strChoice == "4":
            print("Goodbye!")
            break
    except Exception as e:
        print("There was an error.  Check File Permissions.")
        print("The Python error message is: ")
        print(e, e.__doc__, type(e), sep='\n')

# Main Body of Script  ---------------------------------------------------- #
