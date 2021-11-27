import csv
from collections import defaultdict
"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

calls_duration = defaultdict(int)
for record in calls:
    caller = record[0]
    receiver = record[1]
    duration = int(record[3])
    calls_duration[caller] += duration
    calls_duration[receiver] += duration

longest_time_on_phone = max(calls_duration.values())

def get_phone_number():
    for key,value in calls_duration.items():
        if value == longest_time_on_phone:
            return key


print(f"{get_phone_number()} spent the longest time, {longest_time_on_phone} seconds, on the phone during September 2016.")

# Big O:
# O(n) because it is iterating through the files (same as task1).


