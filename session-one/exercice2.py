# Time converter Minutes to hours and minutes

total_minutes = int(input(" Please enter a number in minutes: "))

days = total_minutes // 1440 
hours = total_minutes // 60
minutes = total_minutes % 60

print(f"{total_minutes} minutes is {hours} hour and {minutes} minutes ")