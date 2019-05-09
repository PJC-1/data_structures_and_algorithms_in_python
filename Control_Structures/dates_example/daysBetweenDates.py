# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
#

def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def daysInMonth(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 \
        or month == 8 or month == 10 or month == 12:
            return 31
    else:
        if month == 2:
            return 28
        else:
            return 30

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1), "inputs are not valid"
    # YOUR CODE HERE!
    days = 0
    current_date = year1, month1, day1
    target_date = year2, month2, day2
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
       next_day = nextDay(year1, month1, day1)
       day1 = next_day[2]
       month1 = next_day[1]
       year1 = next_day[0]
       current_date = year1, month1, day1
       days += 1
    return days

def test():
    # tests with 30-day months
    assert daysBetweenDates(2013, 1, 1, 2013, 1, 1) == 0
    assert daysBetweenDates(2013, 1, 1, 2013, 1, 2) == 1
    assert daysBetweenDates(2013, 1, 1, 2014, 1, 1) == 365
    assert nextDay(2013, 1, 1) == (2013, 1, 2)
    assert nextDay(2013, 4, 30) == (2013, 5, 1)
    assert nextDay(2012, 12, 31) == (2013, 1, 1)
    assert nextDay(2013, 2, 28) == (2013, 3, 1)
    assert nextDay(2013, 9, 30) == (2013, 10, 1)
    print ("Tests finished.")

# def test():
#     test_cases = [((2012,9,30,2012,10,30),30),
#                   ((2012,1,1,2013,1,1),360),
#                   ((2012,9,1,2012,9,4),3)]
#
#     for (args, answer) in test_cases:
#         result = daysBetweenDates(*args)
#         if result != answer:
#             print ("Test with data:", args, "failed")
#         else:
#             print ("Test case passed!")

test()
