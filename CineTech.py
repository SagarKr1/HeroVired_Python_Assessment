# Name = Sagar Kumar
# University = AISECT University, Hazaribag
# Git = https://github.com/SagarKr1/HeroVired_Python_Assessment.git

# Note : It is recommended to read the README.md file.
# Read the README.md file to better understand the project's control flow.

# Using the pandas library for formatting data.
import pandas as pd

# Generating a random number .
import random

# Lambda function for updatings salary.
update_salary = lambda salary, percentage: salary * (1 + percentage / 100)


# Business Sales Analytics
def sales_analytics():
    tax_prices = []
    for price in sales:
        tax_prices.append(round(price * 1.1, 2))

    high_value_transactions = []
    for price in sales:
        if price > 500:
            high_value_transactions.append(price)

    total_revenue = 0
    for price in tax_prices:
        total_revenue += price

    # Print results
    print("Tax-inclusive prices(assuming a tax rate of 10%):", tax_prices)
    print("High-value transactions(above $500):", high_value_transactions)
    print(f"Total Revenue after tax: ${total_revenue:.2f}")


# View All Employee
def employee_data():
    global employee

    print("----------------------------------------")
    print("              Employees Data          ")
    print("----------------------------------------")
    if len(employee) <= 0:
        print("No Data Found")
        return

    employee.sort(key=lambda emp: emp["salary"])
    # print(employee)
    df = pd.DataFrame(employee)
    print(df)
    return


# sort employee based on salary
def emp_salary(salary):
    print("-----------------------------------------------")
    print("              Filter employee data          ")
    print("-----------------------------------------------")
    print(salary)
    newlist = []
    if len(employee) <= 0:
        print("No Data Found")
        return

    for emp in employee:
        if emp["salary"] > salary:
            newlist.append(emp)

    if not newlist:
        print("No Data Found")
        return

    df = pd.DataFrame(newlist)
    print(df)
    return


# View All Ticket
def All_Ticket():
    total = 0
    print("------------------------------------")
    print("              Your Bill          ")
    print("------------------------------------")
    if len(Ticket) <= 0:
        print("No Data Found")
        return
    for i in Ticket:
        total = total + i["Final Amount"]
    df = pd.DataFrame(Ticket)
    print(df)
    print(f"Total Amount: {round(total,2)}")
    return


# Search Ticket by ID
def Ticket_ID(data):
    info = {}
    for i in Ticket:
        if i["Ticket ID"] == data:
            info.update(i)
            break
        if i["Student"] == "YES":
            if i["Student_ID"] == data:
                info.update(i)
                break
    if not info:
        print("Data Not Found.\n")
    else:
        df = pd.DataFrame([info])
        print(f"{df}\n")
    return


# Generating a random number for ID.
def random_number():
    return random.randint(1000, 9999)


# Student Discount Function
def student_discount(grade):
    if grade >= 95:
        return 5 / 100
    elif grade >= 85 and grade < 95:
        return 4 / 100
    elif grade >= 75 and grade < 85:
        return 3 / 100
    elif grade >= 65 and grade < 75:
        return 2 / 100
    else:
        return 0


# Deposit balance
def deposit(add_balance):
    global Balance
    if add_balance <= 0:
        print(f"-----> Invalid input. Please enter a valid number. ")
        return 0
    Balance = Balance + add_balance


# Withdraw balance
def withdraw(sub_balance):
    global Balance
    # if balance is zero or smaller than zero
    if sub_balance <= 0:
        print(f"-----> Invalid input. Please enter a valid number. ")
        return 0
    # if balance is zero or smaller than zero
    if Balance <= 0:
        print("Insufficient Balance")
        return 0
    # If the current balance is smaller than the withdrawal amount.
    if Balance < sub_balance:
        print("Insufficient Balance")
        return Balance

    Balance = round(Balance - sub_balance, 2)


# View All Ticket Price
def discount_price():
    print("\n           Ticket Price")
    print("---------------------------------------")
    print("Age Group   | Ticket Price")
    print(" 0-5        |     Free")
    print(" 6-11       |      $5")
    print(" 12-17      |      $8")
    print(" 18-59      |      $12")
    print(" 60-above   |      $7")

    print("\n   Special discount for students")
    print("---------------------------------------")
    print("Grade       |   Discount")
    print(" above 95   |     5%")
    print(" 85-94      |     4%")
    print(" 75-84      |     3%")
    print(" 65-74      |     2%")
    print(" below 64   |     0%")


# Find the ticket price based on age.
def ticket_price(age):
    print("Your age is ", age)
    if age <= 5:
        return 0
    elif age > 5 and age < 12:
        return 5
    elif age >= 12 and age < 18:
        return 8
    elif age >= 18 and age < 60:
        return 12
    else:
        return 7


# Global Variables for Operation
Balance = 0
Ticket = []
# Some predefined data for the employee.
employee = [
    {"Emp-ID": "101", "name": "Alice", "salary": 50000},
    {"Emp-ID": "102", "name": "Bob", "salary": 60000},
    {"Emp-ID": "103", "name": "Charlie", "salary": 70000},
]
# Some predefined data for the sales.
sales = [200, 450, 700, 150, 900]

# The main function of this program starts from here.
while True:
    # description
    print("\nPlease read the README.md file.")
    print("Choose any option")

    print(
        "1. User (Ticket Booking, Financial Transactions, and Student Discounts) \n2. Admin (Employee Salary Management and Business Sales Analytics)\n9. Exit\n"
    )
    # Error Handling
    try:
        # user input for any option
        n = int(input("Enter you choice: "))
        match (n):
            case 1:  # This for User
                while True:
                    print("\nWelcome to CineTech Solutions")
                    print("\n1. Balance/Wallet \n2. Ticket \n7. Back\n")
                    try:
                        u = int(input("Enter your choice: "))
                        match (u):
                            case (
                                1
                            ):  # This is for Wallet Management (Deposit,Withdraw and Check Balance)
                                while True:
                                    try:
                                        print(
                                            "\nChoose an option:\n1. Deposit\n2. Withdraw\n3. Check Balance \n7. Back\n"
                                        )
                                        B = int(input("Enter Your Choice: "))
                                        match (B):
                                            case 1:  # Deposit Balance
                                                print("\nDeposit Balance")
                                                try:
                                                    amount = float(
                                                        input(
                                                            "Enter the amount to add to the balance: "
                                                        )
                                                    )
                                                    # function call
                                                    deposit(amount)
                                                    print(
                                                        f"Your current Balance is ${Balance}.\n"
                                                    )
                                                except ValueError:
                                                    print(
                                                        "\nInvalid input! Please enter a number.\n"
                                                    )

                                            case 2:  # This is Withdraw from the balance
                                                print("\nWithdraw Balance")
                                                try:
                                                    amount = float(
                                                        input(
                                                            "Enter the amount to withdraw from the balance: "
                                                        )
                                                    )
                                                    # function call
                                                    withdraw(amount)
                                                    print(
                                                        f"Your current Balance is ${Balance}."
                                                    )
                                                except ValueError:
                                                    print(
                                                        "\nInvalid input! Please enter a number.\n"
                                                    )

                                            case 3:  # Check your current balance
                                                print(
                                                    f"\nYour Current Balance is ${Balance}\n"
                                                )

                                            case 7:  # Back from wallet
                                                break

                                            case default:  # If no case match
                                                print(
                                                    "\nInvalid Input! Enter given Option.\n"
                                                )
                                    except ValueError:  # Handling error
                                        print(
                                            "\nInvalid input! Please enter a number.\n"
                                        )

                            case 2:  # This is for Ticket Booking
                                while True:
                                    # If the wallet is empty, you need to add funds to your wallet
                                    if Balance == 0:
                                        print(
                                            "\n--------> Insufficient balance. Please add funds to your wallet."
                                        )
                                        break
                                    # If the wallet has some funds.
                                    try:
                                        print("\nChoose an option:")
                                        print(
                                            "0. View Ticket Price(discount and price)\n1. Book Ticket\n2. View Ticket\n3. Search Ticket by ID (Student ID or Ticket ID).\n7. Back\n"
                                        )
                                        check_t = int(input("Enter your choose: "))
                                        match (check_t):
                                            case 0:# show discount and price
                                                discount_price()

                                            case 1:  # Book Ticket
                                                t_num = int(
                                                    input(
                                                        "Enter the number of tickets you want to book: "
                                                    )
                                                )
                                                print(
                                                    "\nEnter the following details: \n"
                                                )
                                                temp_ticket = []
                                                for i in range(0, t_num):
                                                    print(
                                                        f"\nEnter details for user {i+1}."
                                                    )
                                                    name = input("Enter name: ")
                                                    age = int(input("Enter age: "))
                                                    # function call
                                                    price = ticket_price(age)
                                                    student = "NOT"
                                                    grade = 0
                                                    discount = 0
                                                    final_price = 0
                                                    check_stud = 0
                                                    stud_id = 0
                                                    if age > 5:
                                                        print(
                                                            "Confirm, Student or Not\n1. YES\n2. NO"
                                                        )
                                                        check_stud = int(
                                                            input("Student or Not? ")
                                                        )
                                                        # if user will be student
                                                        if check_stud == 1:
                                                            student = "YES"
                                                            while True:
                                                                check_point = 0
                                                                stud_id = input(
                                                                    "Enter Student ID: "
                                                                )
                                                                for i in temp_ticket:
                                                                    if (
                                                                        i["Student"]
                                                                        == "YES"
                                                                    ):
                                                                        if (
                                                                            i[
                                                                                "Student_ID"
                                                                            ]
                                                                            == stud_id
                                                                        ):
                                                                            print(
                                                                                "ID already exists. Please check one."
                                                                            )
                                                                            check_point = (
                                                                                1
                                                                            )
                                                                            continue

                                                                for i in Ticket:
                                                                    if (
                                                                        i["Student"]
                                                                        == "YES"
                                                                    ):
                                                                        if (
                                                                            i[
                                                                                "Student_ID"
                                                                            ]
                                                                            == stud_id
                                                                        ):
                                                                            print(
                                                                                "ID already exists. Please check one."
                                                                            )
                                                                            check_point = (
                                                                                1
                                                                            )
                                                                            continue
                                                                if check_point == 0:
                                                                    break
                                                            print(
                                                                "Enter Marks of following Subject: "
                                                            )
                                                            # Generating grade
                                                            grades_input = input(
                                                                "Enter grades separated by commas: "
                                                            )
                                                            # seprating grade by comma (,)
                                                            grades = [
                                                                int(grade.strip())
                                                                for grade in grades_input.split(
                                                                    ","
                                                                )
                                                            ]
                                                            # sum of all grades
                                                            average_grade = sum(
                                                                grades
                                                            ) / len(grades)
                                                            grade = round(
                                                                average_grade, 2
                                                            )
                                                            print(
                                                                f"Total percentage is {grade}%."
                                                            )
                                                            # print(grade)
                                                            # function call
                                                            st_dis = student_discount(
                                                                grade
                                                            )
                                                            # print("Discount: ", st_dis)
                                                            # Calculation discount
                                                            if st_dis > 0:
                                                                discount = (
                                                                    price * st_dis
                                                                )
                                                                discount = round(
                                                                    discount,
                                                                    2,
                                                                )
                                                                # print(
                                                                #     "Discount: ",
                                                                #     discount,
                                                                # )

                                                        final_price = price - discount
                                                    # Generating ticket data.
                                                    if check_stud == 1:
                                                        temp_ticket.append(
                                                            {
                                                                "Ticket ID": f"ID-{random_number()}",
                                                                "Name": name,
                                                                "Age": age,
                                                                "Student": student,
                                                                "Student_ID": stud_id,
                                                                "Percentage": f"{grade}%",
                                                                "Price": f"${price}",
                                                                "Discount": f"${discount}",
                                                                "Final Amount": final_price,
                                                            }
                                                        )
                                                    else:
                                                        temp_ticket.append(
                                                            {
                                                                "Ticket ID": f"ID-{random_number()}",
                                                                "Name": name,
                                                                "Age": age,
                                                                "Student": student,
                                                                "Price": f"${price}",
                                                                "Discount": f"${discount}",
                                                                "Final Amount": final_price,
                                                            }
                                                        )
                                                    print()
                                                print(
                                                    "---------------------------------------------------"
                                                )
                                                print(
                                                    "                    Your Bill          "
                                                )
                                                print(
                                                    "---------------------------------------------------"
                                                )
                                                no = 1
                                                total = 0
                                                # Calculation of the total ticket price.
                                                for i in temp_ticket:
                                                    total = total + i["Final Amount"]
                                                # This will Show the Bill of Ticket
                                                df = pd.DataFrame(temp_ticket)
                                                print(df)
                                                print(
                                                    f"Total Amount: ${round(total,2)}\n"
                                                )
                                                # If the balance is insufficient to pay the ticket price.
                                                if Balance < total:
                                                    print(
                                                        "Insufficient balance. Please add funds to your wallet, then try booking the ticket again."
                                                    )
                                                    continue
                                                # function call
                                                withdraw(total)
                                                Ticket.extend(temp_ticket)

                                            case 2:  # View Ticket
                                                # function call
                                                All_Ticket()

                                            case (
                                                3
                                            ):  # Search Ticket by ID (Student ID or Ticket ID).
                                                if len(Ticket) <= 0:
                                                    print(
                                                        "\n--------------->Empty Data Found"
                                                    )
                                                    continue
                                                data = input(
                                                    "Enter ID(Student ID or Ticket ID): "
                                                )
                                                print(
                                                    "------------------------------------"
                                                )
                                                print(
                                                    "              Search Data          "
                                                )
                                                print(
                                                    "------------------------------------"
                                                )
                                                # function call
                                                Ticket_ID(data)
                                            case 7:
                                                break

                                            case default:
                                                print(
                                                    "Invalid Input! Enter given Option.\n"
                                                )
                                    except ValueError:
                                        print(
                                            "Something went wrong! Please enter a number\n"
                                        )

                            case 7:
                                break

                            case default:
                                print("Invalid Input! Enter given Option.\n")
                    except ValueError:
                        print("Invalid input! Please enter a number.\n")

            case 2:  # This for Admin
                while True:
                    print("Admin InterFace")
                    print("1. Employee \n2. Sales\n7. Back\n")
                    try:
                        a = int(input("Enter your choice: "))
                        match (a):
                            case 1:
                                while True:
                                    try:
                                        print("\nEmployee")
                                        print(
                                            "1. Add Employee\n2. View Employees Data\n3. Sort Employees (Based on salary)\n4. Update Salary\n7. back\n"
                                        )
                                        num = int(input("Enter your choice: "))
                                        match num:
                                            case 1:  # Add Employee
                                                print(
                                                    "\nFill in the following details to add an employee."
                                                )
                                                emp_name = input(
                                                    "Enter employee name: "
                                                )
                                                salary = float(
                                                    input("Enter employee salary: ")
                                                )
                                                employee.append(
                                                    {
                                                        "Emp-ID": f"{random_number()}",
                                                        "name": emp_name,
                                                        "salary": salary,
                                                    }
                                                )
                                                print(
                                                    "Employee data has been added successfully.\n"
                                                )

                                            case 2:  # View Employee(All Employees Data)
                                                employee_data()

                                            case 3:  # Sort Employees (Based on salary)
                                                while True:
                                                    try:
                                                        num = float(
                                                            input("Enter salary: ")
                                                        )
                                                        emp_salary(num)
                                                        break
                                                    except ValueError:
                                                        print(
                                                            "\nInvalid input! Please enter a number.\n"
                                                        )

                                            case 4:  # Update Salary
                                                print("Update Salary")
                                                while True:
                                                    try:
                                                        print("Choose your option:")
                                                        print(
                                                            "1. 5%\n2. 10%\n3. Manual Input"
                                                        )
                                                        num = int(
                                                            input("Enter your choice: ")
                                                        )
                                                        df = pd.DataFrame(employee)
                                                        if num == 1:
                                                            print(
                                                                "\n-------->Old Salary List"
                                                            )
                                                            print(df)
                                                            for emp in employee:
                                                                emp["salary"] = (
                                                                    update_salary(
                                                                        emp["salary"], 5
                                                                    )
                                                                )
                                                            print(
                                                                "\n-------->Update Salary List"
                                                            )
                                                            s = pd.DataFrame(employee)
                                                            print(s)
                                                            break
                                                        elif num == 2:
                                                            print(
                                                                "\n-------->Old Salary List"
                                                            )
                                                            print(df)
                                                            for emp in employee:
                                                                emp["salary"] = (
                                                                    update_salary(
                                                                        emp["salary"],
                                                                        10,
                                                                    )
                                                                )
                                                            print(
                                                                "\n-------->Update Salary List"
                                                            )
                                                            s = pd.DataFrame(employee)
                                                            print(s)
                                                            break
                                                        elif num == 3:
                                                            per = float(
                                                                input("Enter a digit: ")
                                                            )
                                                            print(
                                                                "\n-------->Old Salary List"
                                                            )
                                                            print(df)
                                                            for emp in employee:
                                                                emp["salary"] = (
                                                                    update_salary(
                                                                        emp["salary"],
                                                                        per,
                                                                    )
                                                                )
                                                            print(
                                                                "\n-------->Update Salary List"
                                                            )
                                                            s = pd.DataFrame(employee)
                                                            print(s)
                                                            break
                                                        else:
                                                            print(
                                                                "\nInvalid input! Please enter given Option.\n"
                                                            )
                                                    except ValueError:
                                                        print(
                                                            "\nInvalid input! Please enter a number.\n"
                                                        )

                                            case 7:
                                                break

                                            case default:
                                                print(
                                                    "Invalid Input! Enter given Option.\n"
                                                )
                                    except ValueError:
                                        print(
                                            "\nInvalid input! Please enter a number.\n"
                                        )

                            case 2:
                                while True:
                                    try:
                                        print("\nSales")
                                        print(
                                            "1. Add Sale Data\n2. View Sales Data\n3. Analyze Sales Data\n7. back\n"
                                        )
                                        num = int(input("Enter your choice: "))
                                        match num:
                                            case 1:  # Add sale data
                                                while True:
                                                    try:
                                                        num = int(
                                                            input(
                                                                "Enter Data in digit: "
                                                            )
                                                        )
                                                        sales.append(num)
                                                        print(
                                                            "New Sales Data: ", end=" "
                                                        )
                                                        for i in sales:
                                                            print(i, end=" ")
                                                        print()
                                                        break
                                                    except ValueError:
                                                        print(
                                                            "\nInvalid input! Please enter a number.\n"
                                                        )

                                            case 2:  # View Sales Data
                                                print("Sales Data: ", end=" ")
                                                for i in sales:
                                                    print(i, end=" ")
                                                print()

                                            case 3:  # Analyze Sales Data
                                                sales_analytics()

                                            case 7:
                                                break

                                            case default:
                                                print(
                                                    "Invalid Input! Enter given Option.\n"
                                                )

                                    except ValueError:
                                        print(
                                            "\nInvalid input! Please enter a number.\n"
                                        )

                            case 7:
                                break

                            case default:
                                print("Invalid Input! Enter given Option.\n")
                    except ValueError:
                        print("Invalid input! Please enter a number.\n")

            case 9:
                print("Exit")
                break

            case default:
                print("Invalid Input! Enter given Option.\n")
    except ValueError:
        print("Invalid input! Please enter a number.\n")
