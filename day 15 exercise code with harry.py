import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = int(time.strftime('%H'))
print(timestamp)
timestamp = int(time.strftime('%M'))
print(timestamp)
timestamp = int(time.strftime('%S'))
print(timestamp)
if 5 < timestamp > 12:
    print("Good Morning")
elif 12 < timestamp > 18:
    print("Good Afternoon")
elif 18 < timestamp > 19:
    print("Good Evening")
else:
    print("Good Night")




