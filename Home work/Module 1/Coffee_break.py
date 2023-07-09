Input_croissants = 4
Input_cups = 5
Input_coffee = 6
Output_dollars = 32
Output_cents = 3238

price_croissants = 1.04
price_cups = 0.34
price_coffee = 4.42

cost_croissants = price_croissants * Input_croissants
cost_cups = price_cups * Input_cups
cost_coffee = price_coffee * Input_coffee

var_total = cost_croissants + cost_cups + cost_coffee
total_dollars = int(var_total)
total_cents = int(var_total * 100)

print('var_total', var_total)
print('total_dollars :', total_dollars)
print('total_cents :', total_cents)

