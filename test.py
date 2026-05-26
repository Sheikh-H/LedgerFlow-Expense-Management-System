from datetime import datetime

month = "January"

value = datetime.strptime(month, "%B").month

print(value)