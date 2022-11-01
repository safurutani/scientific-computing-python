def add_time(start, duration, day = None):
    daysLater = ""
    newDay = ""
    week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    #determine if starting in AM or PM
    if start[-2] == "A":
        startAM = True
        am_pm = " AM"
    else:
        startAM = False
        am_pm = " PM"

    #turn starting and duration time into integers of hours/mins
    startHr = int(start[:start.index(":")])
    startMin = int(start[start.index(":") + 1: start.index(":") + 3])

    addHr = int(duration[:duration.index(":")])
    addMin = int(duration[duration.index(":") + 1: duration.index(":") + 3])

    #adjusting the hour if minutes carry over
    if startMin + addMin > 60: startHr += 1
    newHr = startHr + addHr
    halfDays = int(newHr / 12)

    #correcting the new AM or PM time
    if not startAM: military = (12 + newHr) % 24
    else: military = newHr % 24
    if military < 12: am_pm = " AM"
    else: am_pm = " PM"


    #adjusting minute format to include 0
    newMin = (startMin + addMin) % 60
    if newMin < 10: newMin = "0" + str(newMin)

    if day is not None:
        day = day.lower()
        i = week.index(day)

    #calculate how many days later by using half days as a benchmark - also finding the new day
    if halfDays == 0 or (halfDays == 1 and startAM):
        daysLater = daysLater + ""
        if day is not None:
            daysLater = ", " + day[0].upper() + day[1:]
    elif (halfDays == 1 and not startAM) or (halfDays == 2 and startAM):
        if day is not None:
            day = week[i + 1]
            daysLater = ", " + day[0].upper() + day[1:]
        daysLater = daysLater + " (next day)"
    else:
        #added 1 to halfDays so it would round up for the number of days
        numDays = int((halfDays + 1)/ 2)

        #cycles through week list to find the correct day based on how many days pass
        if day is not None:
            day = week[(i + numDays) % 7]
            daysLater = ", " + day[0].upper() + day[1:]
        daysLater = daysLater + " (" + str(numDays) + " days later)"

    #adjusting the hour so it isn't 00 but 12 instead
    newHr %= 12
    if newHr % 12 == 0: newHr = 12

    new_time = str(newHr) + ":" + str(newMin) + am_pm + daysLater
    print(new_time)
    return new_time

add_time("2:59 AM", "24:00", "saturDay")