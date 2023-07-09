flat = int(input('Enter number of flat: '))

flats_in_floor = 3
floors_in_build = 5
flats_in_entrance = flats_in_floor * floors_in_build

ind_entr = flat / flats_in_entrance
entrance = flats_in_entrance - (int(flats_in_entrance - ind_entr))
var = abs((entrance * flats_in_entrance - flat) - flats_in_entrance)
input = var

ind = input / flats_in_floor
floor = floors_in_build - (int(floors_in_build - ind))


print(f'Flat number {flat} located in the {entrance} entrance on {floor} floor')
