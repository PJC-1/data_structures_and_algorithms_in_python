def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.
    """

    # days = number of days in month1 - day1
    # month1 += 1
    # while month1 < month2:
        # days += number of days in month1
        # month1 += 1
    # days += day2
    # while year1 < year2:
        # days += number of days in that year

    # return days

def testDaysBetweenDates():

    # test same day
    assert(daysBetweenDates(2017, 12, 30,
                              2017, 12, 30) == 0)
    # test adjacent days
    assert(daysBetweenDates(2017, 12, 30,
                              2017, 12, 31) == 1)
    # test new year
    assert(daysBetweenDates(2017, 12, 30,
                              2018, 1,  1)  == 2)
    # test full year difference
    assert(daysBetweenDates(2012, 6, 29,
                              2013, 6, 29)  == 365)

    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")

testDaysBetweenDates()
