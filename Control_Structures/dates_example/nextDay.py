###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    next_day = day
    next_month = month
    next_year = year
    result = None
    next_day += 1
    if next_day > 30:
        next_day = 1
        next_month += 1
    if next_month > 12:
        next_month = 1
        next_year += 1
    return next_year, next_month, next_day
