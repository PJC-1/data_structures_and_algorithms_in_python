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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
total_numbers = set()

for text in texts:
    total_numbers.add(text[0])
    total_numbers.add(text[1])
for call in calls:
    total_numbers.add(call[0])
    total_numbers.add(call[1])

print("There are {} different telephone numbers in the records.".format(len(total_numbers)))

# BIG O notation
# O(n)
