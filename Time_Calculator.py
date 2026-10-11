day_to_index = {
    "monday": 0,
    "tuesday": 1,
    "wednesday": 2,
    "thursday": 3,
    "friday": 4,
    "saturday": 5,
    "sunday": 6
}

index_to_day = {
    0: "monday",
    1: "tuesday",
    2: "wednesday",
    3: "thursday",
    4: "friday",
    5: "saturday",
    6: "sunday"
}

def extract_time(time):
    parts = time.split()
    hour_time = parts[0]
    meridium = parts[1] if len(parts)>1 else None
    hours, minutes = map(int,hour_time.split(":"))
    if meridium == "PM":
        hours += 12
    return [hours, minutes]

def sum_time (start, duration):
    results = [x+y for x,y in zip(extract_time(start),extract_time(duration))]
    hours = results[0]+results[1]//60
    days = hours//24
    minutes = results[1]%60

    return [hours,minutes,days]

def return_day(start_day,day_shift):
    if start_day is not None:
        start_day = start_day.lower()
        index = (day_to_index[start_day]+day_shift%7)%7
        return (index_to_day[index])
    else:
        return None

def format_output(time_parts,final_day):
    final_hour = time_parts[0]%12
    if final_hour == 0:
        final_hour = 12
    final_minute = time_parts[1]
    meridium = "PM" if time_parts[0]//12 ==1 else "AM"
    formatted_time = (f'{final_hour}:{final_minute:02} {meridium}')
    
    if final_day is not None:
        formatted_time += f", {final_day.capitalize()}"

    days_shifted = time_parts[2]
    if days_shifted == 1:
        formatted_time += " (next day)"
    elif days_shifted >1:
        formatted_time += f" ({days_shifted} days later)"
    return(formatted_time)
    

def add_time(start, duration, day=None):   
    new_time = sum_time (start,duration)
    new_day = (return_day(day,new_time[2]))

    new_time = format_output(new_time,new_day)
    return new_time

print(add_time('8:16 PM', '466:02', 'tuesday'))
print(add_time('8:16 PM', '466:02'))
print(add_time('3:30 PM', '2:12', 'Monday'))