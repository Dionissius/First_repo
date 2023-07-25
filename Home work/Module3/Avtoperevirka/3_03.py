base_rate = 40
price_per_km = 10
total_trip = 0


def calculate_trip_price(distance_km):
    global total_trip
    total_trip += 1
    print(distance_km * price_per_km + base_rate)
    return distance_km * price_per_km + base_rate

print(total_trip)
calculate_trip_price(10)
print(total_trip)
calculate_trip_price(25)
print(total_trip)
