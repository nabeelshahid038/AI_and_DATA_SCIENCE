print("Welcome To Personal Expense Tracker System")
print(f"{100*"-"}")
while True:
  try:
    print("1. Add Expenses\n2. View Expenses\n3. Total Expenses\n4. Search By Category\n0. Exit ")
    choice = int(input("Enter your choice : "))
    if choice == 1:
      with open("1.expenses.txt","a") as file:
        print(f"{100*"-"}")
        date = input("Enter Date (DD/MM/YY) : ")
        file.write(date + ",")
        print(f"{100*"-"}")
        category = input("Enter Category (Food, Travel, Shopping, etc.) : ")
        file.write(category.lower() + ",")
        print(f"{100*"-"}")
        amount = input("Enter Amount : ")
        file.write(amount + "\n")
        print(f"{100*"-"}\n")

    elif choice == 2:
      with open("1.expenses.txt","r") as file:
        print(f"{100*"-"}")
        print("Total EXPENSES : ")
        print(f"{100*"-"}")
        print("Date\t\tCategory\t\tAmount")
        print(f"{100*"-"}")
        for line in file.readlines():
          arr = line.split(",")
          for i in range(0,len(arr)):
            if i == (len(arr) - 1):
              print(arr[i])
              break
            print(f"{arr[i]}\t\t",end="")
        print(f"{100*"-"}")

    elif choice == 3:
      with open("1.expenses.txt","r") as file:
        total_amount = 0
        for line in file.readlines():
          arr = line.split(",")
          total_amount += int(arr[-1].strip())
        print(f"{100*"-"}")
        print(f"Total Amount Spent : {total_amount}\n")
        print(f"{100*"-"}")

    elif choice == 4:
      print(f"{100*"-"}")
      category = input("Enter Category to Search Expenses (Food, Travel, Shopping, etc.) : ")
      with open("1.expenses.txt","r") as file:
        print("\nDate\t\tCategory\t\tAmount")
        print(f"{100*"-"}")
        for line in file.readlines():
          arr = line.split(",")
          if category.lower() in arr:
            for i in range(0,len(arr)):
              if i == (len(arr) - 1):
                print(arr[i])
                break
              print(f"{arr[i]}\t\t",end="")
            print(f"{100*"-"}")


    elif choice == 0:
      print(f"{100*"-"}")
      print("\nThank you for using our system!")
      break
    else:
      print("\nINVALID CHOICE : PLEASE ENTER AGAIN!\n")
  except Exception as e:
    print("\nINVALID INPUT!!\n")
