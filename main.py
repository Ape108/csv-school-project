'''
Cameron & Ashton 
'''
import csv

def salaryAvg(csv_file):
    total = 0
    terms = 0
    salary_reader = list(csv.reader(csv_file, delimiter=","))
    for row in salary_reader:
        if row == salary_reader[0]:
            continue
        total += int(row[1])
        terms += 1
    average = round(total / terms, 2)
    return average

def maxRecord(csv_file):
    maxValue = 0
    name = None
    sales_reader = list(csv.reader(csv_file, delimiter=","))
    for row in sales_reader:
        if row == sales_reader[0]:
            continue
        if maxValue < int(row[2]):
            maxValue = int(row[2])
            name = row[0]
    return (maxValue, name)

file_name = ''
while file_name == '':
    file_name = input("Please Enter the name of the file: ")
    try:
        with open(file_name, "r") as my_file:
            choice = None
            while choice == None:
                choice = input("Would you like to calculate the average salary, or the highest sales record?\nPlease Enter 1 or 2: ")
                if choice == '1':
                    salary_average = salaryAvg(my_file)
                    print(f"The average salary is: \n${salary_average}")
                    with open("output.txt", "w") as output_file:
                        output_file.write(f"${salary_average}")
                elif choice == '2':
                    highest_record, name = maxRecord(my_file)
                    print(f"{name} had the highest sales record: \n${highest_record}")
                    with open("output.txt", "w") as output_file:
                        output_file.write(f"{name}, ${highest_record}")
                else:
                    print("Please enter 1 or 2.")
                    choice = None

    except (FileNotFoundError, IOError):
        print("File does not exist. Please enter a valid file name.")
        file_name = ''
    """
    except:
        print("Error retrieving file. Please try again.")
        file_name = ''
    """


