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


