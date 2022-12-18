# shipment and postage calculator
#ask if its a letter or a parcel
type_of_shipment = input("Is it a letter or a parcel? Enter l or p. ").lower()
weight = float(input('Enter the weight: '))
letter_base_cost = 0.05 # 5cents converted to euro
parcel_base_cost = 2
# calculating the various shipment costs and the extra cost perr 100g
if (type_of_shipment == 'l') and (weight <= 200):
    print(f'Total cost: {letter_base_cost}€')
#if the shipment is a letter and weight is between 200g and 500g, add 4cents per 100g
elif (type_of_shipment == 'l') and (weight <= 500):
    extra_cost = weight * 0.04
    print(f'extra cost:{extra_cost} cents')
    total_cost = letter_base_cost + extra_cost
    print(f'Total cost: {total_cost}cents')
#if the shipment is a letter and weight is over 500g, add 7cents per 100g
elif (type_of_shipment == 'l') and (weight > 500):
    extra_cost = weight * 0.07
    total_cost = letter_base_cost + extra_cost
    print(f'extra_cost:{extra_cost}cents')
    print(f'Total_cost:{total_cost}cents')
# if the type of shipment is a parcel,p the base cost is €2
elif(type_of_shipment == 'p') and (weight <= 200):
    print(f'Total_cost: {parcel_base_cost}€')
elif (type_of_shipment == 'p') and (weight <= 500):
    extra_cost = weight * 0.08
    print(f'extra cost:{extra_cost} cents')
    total_cost = parcel_base_cost + extra_cost
    print(f'Total cost: {total_cost}€')
#if weight is graeter than 500g
else:
    extra_cost = weight * 0.14
    print(f'extra cost:{extra_cost} cents')
    total_cost = parcel_base_cost + extra_cost
    print(f'Total cost: {total_cost}€')



