import json
import os

print("\n")
print("===== Expense Tracker =====\n\n")
print("1. Add expense \n2. View Expense \n3. Total Expense \n4. Delete Expense\n5. Exit\n")

exp_data = {}

 
if os.path.exists("data.json"):
      try:
            with open("data.json" , "r") as f:
                  exp_data = json.load(f)
      except json.JSONDecodeError as e:
            print("Invalid JSON syntax ", e)
            with open("data.json" , "w") as f:
                  json.dump(exp_data, f)


else:
      with open("data.json", "w") as f:
        json.dump(exp_data, f)

def addExpense(exp_data):
        expense_name = input("Expense name: ").title()
        expense_amount = int(input("Amount: "))
        if expense_name not in exp_data:
            exp_data[expense_name] = expense_amount
        else:
              exp_data[expense_name] += expense_amount



def viewExpense(exp_data):
      for keys in exp_data:
            print(keys, " - ", exp_data[keys])
      

def viewTotal(exp_data):
      total = 0
      for keys in exp_data:
            total = total + exp_data[keys]

      return total

def deleteExpense(exp_data):
      dlt_exp = input("Enter the expense to delete: ").title()
      if dlt_exp in exp_data:
            exp_data.pop(dlt_exp)
            print("Expense ", dlt_exp, " deleted\n")
      else:
            print("\n" , dlt_exp , " is not in your expenses\n")

def saveFile(exp_data):
      with open("data.json" , "w") as f:
            json.dump(exp_data, f)



while True:

    user_command = input("Enter your Choice: ")
    

    if user_command == "1":
        addExpense(exp_data)
        print("\nEpense Added\n")
        saveFile(exp_data)

    elif user_command == "2":
          print("\n===== Your Expenses =====\n")
          viewExpense(exp_data)
          print("\n")
          

    elif user_command == "3":
          print(f'\nTotal: ₹{viewTotal(exp_data)}\n')
          

    elif user_command == "4":
          deleteExpense(exp_data)
          saveFile(exp_data)
          

    elif user_command == "5":
          saveFile(exp_data)
          break

    else:
          print("\nInvalid command\n")

    
