from datetime import datetime, time

"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

text_line = texts[0]
complete_date = text_line[2]
only_time = datetime.strptime(complete_date, "%m-%d-%Y %H:%M:%S").time()

print(f"First record of texts, {text_line[0]} texts {text_line[1]} at time {only_time}")

call_line = calls[-1]
call_date = call_line[2]
call_time = datetime.strptime(call_date, "%d-%m-%Y %H:%M:%S").time()

print(f"Last record of calls, {call_line[0]} calls {call_line[1]} at time {call_time}, lasting {call_line[-1]} seconds")

# Big O:
# I think here would be O(1).
