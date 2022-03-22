#importing libraries
import os
import time
import datetime
import tabulate
import csv

# welcome and go to menu
print("Welcome to Harkov Daily Program Report")
print("==================================")

# show current time and date
print("Current time and date is: " + str(datetime.datetime.now()))

# show menu and user can choose
print("1. Create")
print("2. Read")
print("3. Update")
print("4. Delete")
print("5. Exit")

# user choose menu
menu = int(input("Please choose menu: "))
if menu == 1:
    # create data for table and save the record
    print("Create")
    print("======")
    print("1. Create a new record")
    print("2. Back to menu")
    create = int(input("Please choose menu: "))
    if create == 1:
        # create a new record
        print("Create a new record")
        print("==================")
        # user input data
        no = int(input("No: "))
        date = input("Date: ")
        project_status = input("Project Status: ")
        # save data into a list
        data = [no, date, project_status]
        # save data into a table
        table = [data]
        # show data in a table
        print("Data in a table")
        print("================")
        print(tabulate.tabulate(table, headers=["No", "Date", "Project Status"]))
        print("")
        # user choose to save data or not
        save = input("Do you want to save this record? (y/n): ")
        if save == "y":
            # save data into a csv file
            with open("data.csv", "a") as file:
                writer = csv.writer(file)
                writer.writerow(data)
            print("Data has been saved")
            print("")
        else:
            print("Data has not been saved")
            print("")
        
            
    elif create == 2:
        # back to menu
        print("Back to menu")
        print("============")
        print("")
    else:
        print("Invalid input")
        print("")
    
elif menu == 2:
    # open csv file and show data in a table
    print("Read")
    print("====")
    print("1. Show all data")
    print("2. Back to menu")
    read = int(input("Please choose menu: "))
    if read == 1:
        # open csv file and show data in a table
        print("Show all data")
        print("=============")
        # open csv file
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            # show data in a table
            print("Data in a table")
            print("================")
            print(tabulate.tabulate(list(reader), headers=["No", "Date", "Project Status"]))
            print("")
    elif read == 2:
        # back to menu
        print("Back to menu")
        print("============")
        print("")
    else:
        print("Invalid input")
        print("")      

elif menu == 3:
    #edit data for table and save the record
    print("Update")
    print("======")
    print("1. Update a record")
    print("2. Back to menu")
    update = int(input("Please choose menu: "))
    if update == 1:
        # edit data for table and save the record
        print("Update a record")
        print("================")
        # open csv file
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            # show data in a table
            print("Data in a table")
            print("================")
            print(tabulate.tabulate(list(reader), headers=["No", "Date", "Project Status"]))
            print("")
        # user input data
        no = int(input("No: "))
        date = input("Date: ")
        project_status = input("Project Status: ")
        # save data into a list
        data = [no, date, project_status]
        # save data into a table
        table = [data]
        # show data in a table
        print("Data in a table")
        print("================")
        print(tabulate.tabulate(table, headers=["No", "Date", "Project Status"]))
        print("")
        # user choose to save data or not
        save = input("Do you want to save this record? (y/n): ")
        if save == "y":
            # save data into a csv file
            with open("data.csv", "w") as file:
                writer = csv.writer(file)
                writer.writerow(data)
            print("Data has been saved")
            print("")
        else:
            print("Data has not been saved")
            print("")
    elif update == 2:
        # back to menu
        print("Back to menu")
        print("============")
        print("")
    else:
        print("Invalid input")
        print("")
elif menu == 4:
    #delete data for table and save the record
    print("Delete")
    print("======")
    print("1. Delete a record")
    print("2. Back to menu")
    delete = int(input("Please choose menu: "))
    if delete == 1:
        # delete data for table and save the record
        print("Delete a record")
        print("================")
        # open csv file
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            # show data in a table
            print("Data in a table")
            print("================")
            print(tabulate.tabulate(list(reader), headers=["No", "Date", "Project Status"]))
            print("")
        # user input data
        no = int(input("No: "))
        # save data into a list
        data = [no]
        # save data into a table
        table = [data]
        # show data in a table
        print("Data in a table")
        print("================")
        print(tabulate.tabulate(table, headers=["No"]))
        print("")
        # user choose to save data or not
        save = input("Do you want to save this record? (y/n): ")
        if save == "y":
            # save data into a csv file
            with open("data.csv", "w") as file:
                writer = csv.writer(file)
                writer.writerow(data)
            print("Data has been saved")
            print("")
        else:
            print("Data has not been saved")
            print("")
    elif delete == 2:
        # back to menu
        print("Back to menu")
        print("============")
        print("")
    else:
        print("Invalid input")
        print("")

elif menu == 5:
    print("Exit")
else:
    print("Wrong input")
