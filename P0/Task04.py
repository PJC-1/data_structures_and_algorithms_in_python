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
def numbers_list(data, column):
    number_list = []
    for number in data:
        number_list.append(number[column])
    return number_list

caller_list = numbers_list(calls, 0)
answered_call_list = numbers_list(calls, 1)
texter_list = numbers_list(texts, 0)
received_text_list = numbers_list(texts, 1)

telemarketers = sorted(list(set(caller_list) - set(answered_call_list) - set(texter_list) - set(received_text_list)))
print("These numbers could be telemarketers: ")
for number in telemarketers:
    print(number)

# BIG O notation
# O(n)
