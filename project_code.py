print("Monthly Expense Tracker - Prajwal Butte")

monthly_limit = float(input("Enter your monthly limit (₹):"))

expenses = []
category = []

while True:
    print("\nAdd expenses:")
    amount = float(input("Amount spent(₹):"))
    categories = input("Category (e.g.,food,travel):")

    expenses.append(amount)
    category.append(categories)

    total_spent =  sum(expenses)
    print(f"Total spent:{total_spent}₹")

    if total_spent > monthly_limit:
      print("Alert : You have exceeded your budget!")

    choice = input("\nAdd another expense? (yes/no) :").strip().lower()
    if(choice != "yes"):
       break
    
print("\nMonthly Expense:")
for i in range(len(expenses)):
   print(f"{categories[i]}-₹{amount}")
print(f"Total spent:₹{sum(expenses)}")
print(f"Budget limit:₹{monthly_limit}")

if sum(expenses) > monthly_limit:
   print("Budget exceeded!")
else:
   print("Budget is under control!")


print("\n Thank You For Using!")