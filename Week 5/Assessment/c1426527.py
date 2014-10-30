def doomsday(y):
    """
    >>> doomsday(2012)
    3
    >>> doomsday(1899)
    2
    >>> doomsday(1923)
    3
    >>> doomsday(10000)
    -1
    >>> doomsday(1756)
    -1
    >>> type(doomsday(2010))
    <class 'int'>
    """
    #Make sure that the year we are given is between the range that we need
    if y >= 1800 and y < 2200:
        if y < 1900:
            x = 5
        elif y < 2000:
            x = 3
        elif y < 2100:
            x = 2
        elif y < 2200:
            x = 0
    #Define some variables that will be used later
    #Convert the year to a string so that we can slice it
    #Reconvert it back to an int for processing it later
        w = int(str(y)[2:])
        b = w % 12
        a = w // 12
        c = b // 4
        d = (a + b + c) % 7
    #Create a loop that adds one to the x value whilst subracting 1 from d
    #If x equals 6 then subtract 1 from d and set x = 0
        while d > 0:
            if x == 6:
                d = d - 1
                x = 0
            else:
                d = d - 1
                x = x + 1
        return x
    #If outside the year range then just return -1
    else:
        return -1