

buy_1 = float(input(f'Enter cost for 1t buy: $'))
buy_2 = float(input(f'Enter cost for 2d buy: $'))
buy_3 = float(input(f'Enter cost for 3d buy: $'))
buy_4 = float(input(f'Enter cost for 4h buy: $'))

# buy_1 = 34.34
# buy_2 = 12.01
# buy_3 = 17.42
# buy_4 = 4.93

total = buy_1 + buy_2 + buy_3 + buy_4
total_dollars = int(total) 
var = round(total % 1, 2) * 100
total_cents = int(var)

print(f'Price for 1t buy: ${buy_1}')
print(f'Price for 2d buy: ${buy_2}')
print(f'Price for 3d buy: ${buy_3}')
print(f'Price for 4h buy: ${buy_4}')
print()
print(f'TOTAL : {total_dollars} dollars {total_cents} cents')

