

count =  float(input("Enter a number of minutes: "))

total_second = int(count * 60)
hours = total_second // 3600

second_remaining = total_second % 3600

second = count * 60
second_remaining = total_second % 3600

minutes = second_remaining // 60
seconds = second_remaining % 60

print(f"{count} minutes is {hours} hour(s), {minutes} minute(s), and {seconds} second(s).")
