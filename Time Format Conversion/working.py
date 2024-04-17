import re


def main():
    # User input can only be in format X AM/PM to X AM/PM or X:XX AM/PM to X:XX AM/PM
    print(convert(input("Hours: ")))


def convert(s):
    format_match = re.search(
        r"^([0-9][0-9]?)(:)?([0-9][0-9])? ([A|P]M) to ([0-9][0-9]?)(:)?([0-9][0-9])? ([A|P]M)$",
        s,
    )
    if format_match:
        caps = format_match.groups()
        # check hours are not out of range
        if int(caps[0]) > 12 or int(caps[4]) > 12:
            raise ValueError("Incorrect Hours Input")
        # check hours are not a tripple digit,
        # otherwise the regex sources the first digit for the hour and the other 2 digits for the minutes
        # and allows conversion
        if caps[1] == None and caps[2] != None:
            raise ValueError("Incorrect Format")
        if caps[5] == None and caps[6] != None:
            raise ValueError("Incorrect Format")
        # check minutes are not out of range
        if caps[2] != None and int(caps[2]) > 59:
            raise ValueError("Incorrect Minutes Input 1")
        if caps[6] != None and int(caps[6]) > 59:
            raise ValueError("Incorrect Minutes Input 2")
        # format first and second parts of the time into a required format
        from_time = format(caps[0], caps[2], caps[3])
        to_time = format(caps[4], caps[6], caps[7])
        return from_time + " to " + to_time
    else:
        raise ValueError


def format(hrs, mins, am_pm):
    if mins == None:
        f_mins = "00"
    else:
        f_mins = mins
    if am_pm == "AM":
        if int(hrs) == 12:
            f_hrs = "00"
        else:
            f_hrs = f"{int(hrs):02}"
    else:
        if int(hrs) == 12:
            f_hrs = hrs
        else:
            f_hrs = f"{int(hrs) + 12}"

    return f_hrs + ":" + f_mins


if __name__ == "__main__":
    main()
