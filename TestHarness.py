# ---------------------------------------------------------- #
# Title: Listing 08
# Description: A main module for testing
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# ---------------------------------------------------------- #
if __name__ == "__main__":
    import DataClasses as D  # data classes
    import ProcessingClasses as P  # processing classes
    import IOClasses as I  # io classes
else:
    raise Exception("This file was not created to be imported")

# Test data module
# objP1 = D.Person("Bob", "Smith")
objE1 = D.Employee(1,"Bob", "Smith")
# objP2 = D.Person("Sue", "Jones")
objE2 = D.Employee(2,"Sue", "Jones")
lstTable = [objE1, objE2]
for row in lstTable:
    print(row.to_string(), type(row))
# Test data module

# Test processing module
# P.FileProcessor.save_data_to_file("PersonData.txt", lstTable)
# lstFileData = P.FileProcessor.read_data_from_file("PersonData.txt")
# for row in lstFileData:
#   p = D.Person(row[0], row[1])
#   print(p.to_string().strip(), type(p))

P.FileProcessor.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = P.FileProcessor.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(line.strip())
for row in lstTable:
    print(row.to_string(), type(row))
# Test processing module

# Test IO classes
# Done: create and test IO module
I.EmployeeIO.print_menu_items()
I.EmployeeIO.print_current_list_items(lstTable)
print(I.EmployeeIO.input_employee_data())
print(I.EmployeeIO.input_menu_options())
# Test IO classes

