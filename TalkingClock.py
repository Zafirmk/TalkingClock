import datetime
pm = False
TimeInput = datetime.datetime.now()
hours_list = ["Twelve", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven"]
tens_list = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty"]
extra = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
unique = ["", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
hour = TimeInput.hour
minute = TimeInput.minute

if hour in range(12, 24):
    hour = hour - 12
    pm = True

if minute in range(0, 10):
    minute = "0" + str(minute)
if minute in range(11, 20):
    Time = "It's " + hours_list[hour] + unique[minute-10]
else:
    Time = "It's " + hours_list[hour] + tens_list[int(str(minute)[0:1])] + " " + extra[int(str(minute)[1:2])]

if pm == True:
    print(Time + " PM")
else:
    print(Time + " AM")

