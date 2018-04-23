from datetime import datetime
from datetime import timedelta

print("Current datetime")
print(datetime.now())

print("\nCurrent UTC datetime")
print(datetime.utcnow())

print("\nDatetime in 1 year, 5 minutes, 30 seconds")
print(datetime.now() + timedelta(days=365, minutes=5, seconds=30))

print("\nDatetime in readable format")
print(datetime.now().strftime("%a, %d %b %Y %H:%M:%S"))
