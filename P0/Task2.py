"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
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

call_dictionary = {}
max_durration = 0
max_phone_number = {}

for call in calls:
    if (call[0] not in call_dictionary):
        call_dictionary[call[0]] = int(call[3])
    else:
        call_dictionary[call[0]] += int(call[3])

    if (call[1] not in call_dictionary):
        call_dictionary[call[1]] = int(call[3])
    else:
        call_dictionary[call[1]] += int(call[3])

for number in call_dictionary:
    if call_dictionary[number] > max_durration:
        max_durration = call_dictionary[number]
        max_phone_number.clear()
        max_phone_number[number] = call_dictionary[number]
    elif call_dictionary[number] == max_durration:
        max_phone_number[number] = call_dictionary[number]

for item in max_phone_number:
    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(item, max_phone_number[item]))

# BIG O notation
# O(n)
