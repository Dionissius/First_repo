# Программа 
# Узнать сколько часов или секунд или минут в заданном временном отрезке

hours_in_day = 24
minutes_in_day = 1440
sec_in_day = 86400

minutes_in_hour = 60
seconds_in_hour = 3600

seconds_in_minute = 60

input_days = int(input('Please enter number of days: '))
input_hours = int(input('Please enter number of hours: '))
input_minutes = int(input('Please enter number of minutes: '))
input_seconds = int(input('Please enter number of seconds: '))

hours =  (input_days * hours_in_day) + input_hours
minutes = (hours * minutes_in_hour) + input_minutes
seconds = (minutes * seconds_in_minute) + input_seconds 

print()
print(f'So in {input_days} days {input_hours} hours {input_minutes} minutes {input_seconds} seconds, We have:')
print()
print(f'{hours} hours')
print(f'{minutes} minutes')
print(f'{seconds} seconds')


# sec_in_hour = 3600
# sec_in_minutes = 60

# hours = int(sec_input / sec_in_hour)
# rest_after_hours = sec_input - (sec_in_hour * hours)

# minutes = int(rest_after_hours / sec_in_minutes)
# rest_after_minutes = rest_after_hours - (minutes * sec_in_minutes)

# seconds = rest_after_minutes

# print(f'In {sec_input} seconds : {hours} hours {minutes} minutes {seconds} seconds')