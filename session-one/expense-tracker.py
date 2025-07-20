# 🧩 How I broke it down:

# Ask the user for amount + category

# Append the data to a CSV file

# Show total spent that day

# That’s it. No frameworks. No fancy tools.
# Just raw Python and a single .csv file.

# Here’s what I learned by doing it:
# ✅ Working with files
# ✅ Handling user input
# ✅ Writing clean, testable functions
# ✅ Actually finishing something I could reuse


 
# categories = []
# user_input = input("What categories you want to  track today: \n ")

# new_cat= categories.append(user_input) #Append the input to the categories list

# print(new_cat)



import datetime
import csv

user_name = input("before we get started, what is your name? \n")
print(f"{user_name} welcome to your personal expense tracker : ")
current_datetime = datetime.datetime.now().strftime("%Y-%m-%d")
print(f"today's date is {current_datetime}")

cat_list = []

while True: # f7alat kan chart motawfir
    user_category = input(" Enter your categories that's needs to be tracked and enter done to finish : \n").strip().lower()

    if user_category == "done":
        break # stop when the user input done
   
    if user_category in cat_list:
        print("This category already in the list")
   
    else:
        cat_list.append(user_category)

print(f" you final categories are" , cat_list)


amount = float(input("How much did you spend in $ ? "))


while True:
    category = input("which category? ").lower().strip()
    if category in cat_list:
        break
    else:
        print("That category is not in your list. please enter a valid one")
    

#CSV Module
with open("expense.csv",mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([current_datetime, category, amount])

print("expense is recorded")











