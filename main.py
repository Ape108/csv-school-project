'''
Cameron & Ashton 
'''
import csv

def salaryAvg(csv_file):
    salary_reader = csv.reader(csv_file, delimiter=",")
    for row in salary_reader:
        if row == ["Name", "Salary", "Sales"]:
            continue
        print(row)

file_name = ''
while file_name == '':
    file_name = input("Please Enter the name of the file: ")
    try:
        with open(file_name, "r") as my_file:
            salaryAvg(my_file)
            pass

    except (FileNotFoundError, IOError):
        print("File does not exist. Please enter a valid file name.")
        file_name = ''
    except:
        print("Error retrieving file. Please try again.")
        file_name = ''



