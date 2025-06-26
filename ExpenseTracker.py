import csv

def add_expense(exp):
    date = input("Enter Date (YYYY-MM-DD) :")
    category = input("Enter Catergory :")
    amount = input ("Enter Amount :")
    description = input("Enter a brief description :")
    exp.append({
     "Date":date,
     "Category":category,
     "Amount" : amount,
     "Description":description
     })
    print("Expense added successfuly.")


def view_expense(exp):
    if not exp:
        print("No expenses yet.")
    else:
        for expense in exp:
            if all(key in expense for key in ["Date","Category","Amount","Description"]):
                print(f"Date: {expense['Date']},Category: {expense['Category']},Amount: {expense['Amount']},Description: {expense['Description']}")
            else:
                print(f"Invalid expense record: {expense}")



def set_budget():
    budget= float(input("Enter your monthly budget:"))
    return budget


def track_expense(exp,budget):
    total_expense = sum(float(expense["Amount"]) for expense in exp)
    print(f"Total Expenses :{total_expense}")
    if total_expense == budget:
        print("You have used all your budget for this month.")
    elif total_expense > budget:
        print("Warning : You have exceeded your monthly budget!")
    else:
        print(f"Your remaining amount to be used :{budget - total_expense}")


def save_expense(exp, filename = 'expenseTracker.csv'):
    with open(filename,'w',newline = '') as file:
        writer = csv.writer(file);
        writer.writerow(["Date","Category","Amount","Description"])
        for expense in exp:
             writer.writerow([expense['Date'],expense['Category'],expense['Amount'],expense['Description']])
    print("Expense saved successfuly.")


def load(filename = 'expenseTracker.csv'):
    exp = []
    try:
        with open(filename,'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if all(key in row for key in ["Date","Category","Amount","Description"]):
                    row["Amount"] = float(row["Amount"])
                    expense ={
                        "Date" : row["Date"],
                        "Category" : row["Category"],
                        "Amount" : row["Amount"],
                        "Description" : row["Description"]
                        }
                    exp.append(expense)
                else:
                    print(f"Skipping invalid expense : {row}")
    except FileNotFoundError:
        print("Expense file not found. Please create first to load!")
    return exp


def Start():
    expense = load()
    budget = set_budget()
    while True:
        print("\nPersonal Expense Tracker")
        print("1: Add Expenses")
        print("2: View Expenses")
        print("3: Track Budget")
        print("4: Save Expenses")
        print("5: Exit")

        choice = input("Enter your choice :")
        match choice:
            case '1':
                add_expense(expense)
            case '2':
                view_expense(expense)
            case '3':
                track_expense(expense,budget)
            case '4':
                save_expense(expense)
            case '5':
                YesNo = input("Do you want to save before exiting? (Yes/No) :")
                if YesNo == "Yes":
                    save_expense(expense)
                else:
                    print("Exiting.....")
                break
            case _:
                print("Invalid choice. Please select a valid option")

Start()





