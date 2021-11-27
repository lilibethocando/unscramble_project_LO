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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


all_numbers = set()
telemarketing_numbers = set()

for incoming_call in calls:
    all_numbers.add(incoming_call[1])

for text in texts:
    all_numbers.add(text[0])
    all_numbers.add(text[1])

for number in calls:
    if number[0] not in all_numbers:
        telemarketing_numbers.add(number[0])

#print(len(telemarketing_numbers))

for tele_number in sorted(telemarketing_numbers):
    print(tele_number)

# Big O:
# Based on the information provided beforehand fot this project (when using sorted() or list.sort())
# The run time would be O(n log n).



