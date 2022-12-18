euro_dollar = 1.23
euro_pound = 0.89
amount = float(input("Enter amount: "))
currency_name = input("Enter currency name: €/P")
def convert_money(amount, original_currency, target_currency):
    return "You have " + str(amount * exchange_rate) + " " + currency_name + "."
print(convert_money(amount, exchange_rate, currency_name))