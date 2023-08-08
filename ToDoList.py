# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Gail Provancha, 8.6.2023, Added code to complete assignment 5
# ------------------------------------------------------------------------ #
# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection
# -- Processing -- #
# Step 1 - When the program starts, load the data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows.
try:
    objFile = open(objFile, "r")  # open text file
    for row in objFile:  # loop through the rows in the text file
        row = row.split(",")  # split each row by a comma to return a list
        dicRow = {"Task": row[0], "Priority": row[1].strip()}  # strip removes spaces
        lstTable.append(dicRow)  # adds each new dictionary row to a table
    objFile.close()
except:
    print("The file '"+objFile + "'does not exist.")  # if text file does not exist
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Task" + ":" + " Priority")  # Header
        for row in lstTable:
            print(str(row["Task"].title()) + ": " + str(row["Priority"].title()))  # print each row as loops
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Task: ")
        strPriority = input("Priority: ")
        lstTable.append({"Task": strTask, "Priority": strPriority})
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strTask = input("What task do you want to remove? ")  # get user input
        for row in lstTable:
            if row["Task"].lower() == strTask.lower():
                lstTable.remove(row)  # if row matches user input, remove row
                print(strTask + " removed")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", 'w')  # create or open text file
        for row in lstTable:  # loop through the rows in the table
            objFile.write(str(row["Task"].title()) + ',' + str(row["Priority"].title()) + '\n')
        objFile.close()  # close the text file
        print("Data saved for future use")  # Display message to user
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Exiting the Program")
        break  # and Exit the program
