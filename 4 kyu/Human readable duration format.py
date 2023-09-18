def format_duration(seconds):
    temp_list = []

    MINUTE = 60
    HOUR = 60 * MINUTE
    DAY = 24 * HOUR
    YEAR = 365 * DAY

    sec, mint, hour, day, year = 0, 0, 0, 0, 0
    while seconds != 0:
        if seconds >= 31536000:
            year += 1
            seconds = seconds - YEAR

        elif seconds >= 86400:
            day += 1
            seconds = seconds - DAY
        elif seconds >= 3600:
            hour += 1
            seconds = seconds - HOUR
        elif seconds >= 60:
            mint = mint + 1
            seconds = seconds - MINUTE
        elif seconds < 60:
            sec = seconds
            seconds = seconds - seconds
        else:
            break

    duration = [year, day, hour, mint, sec]

    i = 0
    for elem in duration:
        Duration = ["year", "day", "hour", "minute", "second"]
        if elem == 0:
            x = 0
        elif elem == 1:
            temp_list.append(f"{elem} {Duration[i]}")
        else:
            temp_list.append(f"{elem} {Duration[i]}s")
        i = i + 1

    if len(temp_list) == 0:
        return "now"
    elif len(temp_list) == 1:
        return temp_list[0]
    elif len(temp_list) == 2:
        return f"{temp_list[0]} and {temp_list[1]}"
    elif len(temp_list) == 3:
        return f"{temp_list[0]}, {temp_list[1]} and {temp_list[2]}"
    elif len(temp_list) == 4:
        return f"{temp_list[0]}, {temp_list[1]}, {temp_list[2]} and {temp_list[3]}"
    elif len(temp_list) == 5:
        return f"{temp_list[0]}, {temp_list[1]}, {temp_list[2]}, {temp_list[3]} and {temp_list[4]}"
    
# Test Cases

print(format_duration(1))
print(format_duration(62))
print(format_duration(120))
print(format_duration(3600))