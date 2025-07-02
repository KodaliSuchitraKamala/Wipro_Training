from datetime import datetime, date, timedelta
# current time and date
now = datetime.now()
print("Current Datetime", now)
# only date
print("Todays date", date.today()) # it gives us in the format of US
# fromatted datetime of India
formatted = now.strftime("%d-%m-%Y %H:%M:%S") 
print("Formatted datetime", formatted)
formatted = now.strftime("%d-%m-%y %H:%M:%S") 
print("Formatted datetime", formatted)
# parsed datetime
date_str = "24-12-2000 14:55:00"
parsed = datetime.strptime(date_str, "%d-%m-%Y %H:%M:%S")
print("Parsed data: ", parsed)
# timedelta
tommorow = now + timedelta(days = 1)
print("Tommorow: ", tommorow)
yesturday = now - timedelta(days = 1)
print("Yesturday: ", yesturday)
ftime = now + timedelta(hours = 3, minutes = 30)
print("After 3.5 hours: ", ftime)
now = datetime.now()
format_12hr = now.strftime("%d/%m/%Y, %I:%M:%S %p")
print(format_12hr)