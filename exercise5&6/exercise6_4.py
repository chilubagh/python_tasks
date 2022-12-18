
# ask user the price of the food
food_price = float(input('what is the price of the food? '))
print(f'Charge for food = ${food_price}')
# calculate the tip paid on any food bought and round to 2 decimal places
customer_tip = float(input('How much tip was paid? '))
#percentage_of_tip = 18
#tip_paid = round(food_price * 0.18, 2)
#print(f'tip = ${tip_paid}')
print(customer_tip)
# calculate the sales tax of 7 percent on food bought and round to 2 decimal places
sales_tax = round(food_price * 0.07, 2)
print(f'sales tax = ${sales_tax}')
# calculate price if food with tax
food_price_tax = food_price + sales_tax
print(f'food price with tax = ${food_price_tax}')

# calculate the total amount paid on food
grand_total = food_price_tax + customer_tip
print(f'Grand total = ${grand_total}')
