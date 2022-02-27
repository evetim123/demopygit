from datetime import datetime
now = datetime.now()
current_year = now.year
current_day = now.day
current_date = now.date
print(current_year)
print(current_day)
print(current_date)
print('%02d/%02d/%04d' % (now.hour, now.minute, now.second))
