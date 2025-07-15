# # Generate number from one to ten
# import random

# # number = int(random.random() * 100) % 10
# # number = number+1

# # print(number)

# # Exercise: “Change Machine – Coins Breakdown”
# # Description:
# # Write a program that:
# # Asks the user to enter an amount in cents (for example, 137 cents).
# # Calculates the minimum number of coins needed using:
# # 1-euro coins (100 cents)
# # 50-cent coins
# # 20-cent coins
# # 10-cent coins
# # 5-cent coins
# # 1-cent coins
# # Outputs the result: how many of each coin the machine would return.




# amount = int(input(" Enter an amount of in Cents: "))

# euro_1= amount//100
# amount = amount % 100

# cent_50 =amount //50
# amount = amount % 50

# cent_20 = amount //20
# amount = amount %20

# cent_10 = amount // 10
# amount = amount % 10

# cent_5 = amount //5
# amount = amount % 5

# cent_1 = amount // 1
# amount = amount % 1


# print("1-euro coins:", euro_1)
# print("50-cent coins:", cent_50)
# print("20-cent coins:", cent_20)
# print("10-cent coins:", cent_10)
# print("5-cent coins:", cent_5)
# print("1-cent coins:", cent_1)


user_input = int(input("Enter how much dollars bills you have: "))

twenty_usd = user_input // 20
remainder = user_input % 20

ten_usd = remainder // 10
remainder = remainder % 10

five_usd = remainder // 5
remainder = remainder % 5

single_usd = remainder // 1

print(f"{user_input} USD is made of:")
print(f"{twenty_usd} x $20 bills")
print(f"{ten_usd} x $10 bills")
print(f"{five_usd} x $5 bills")
print(f"{single_usd} x $1 bills")


