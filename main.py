# Программа 
# Узнать сколько часов-минут-секунд в веддённом количестве секунд

sec_input = int(input('Please enter sec: '))

sec_in_hour = 3600
sec_in_minutes = 60

hours = int(sec_input / sec_in_hour)
rest_after_hours = sec_input - (sec_in_hour * hours)

minutes = int(rest_after_hours / sec_in_minutes)
rest_after_minutes = rest_after_hours - (minutes * sec_in_minutes)

seconds = rest_after_minutes

print(f'In {sec_input} seconds : {hours} hours {minutes} minutes {seconds} seconds')

# print(hours)
# print(rest_after_hours)
# print()
# print(minutes)
# print(rest_after_minutes)
# print()
# print(seconds)
