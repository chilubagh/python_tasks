# ask the user for amount of money and cost of purchase
amount = float(input("Enter the amount of money: "))
purchase_cost = float(input("Enter the cost of the item: "))

# if the amount is enough on first try, print "thank you" and print the change
if amount >= purchase_cost:
    print(f"Thank you.Here is the Change: {amount - purchase_cost}€")
# if the amount is not enough, ask for more money and print the Change
elif amount < purchase_cost:
    print("Not enough money,give more.")
    more_money = float(input("Enter more money: "))
    change = amount + more_money - purchase_cost
    print(f"Thank you.Here is the Change: {change}€")



