def add_time(start, duration, week=None):
    week_list = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    temp,time = start.split(' ')
    hour,minute = temp.split(':')
    hour,minute = int(hour),int(minute)
    d_hour,d_minute = duration.split(':')
    d_hour,d_minute = int(d_hour),int(d_minute)
    
    minute = minute+d_minute
    hour = hour+12 if time=='PM' else hour
    hour = hour+d_hour+int(minute/60)
    
    day = int(hour/24)
    week =  ', '+week_list[(week_list.index(week.capitalize())+day)%7] if week else ''
    if day==0:
        day = ''
    elif day==1:
        day = ' (next day)'
    else:
        day = ' (%d days later)'%(day)
    time = "AM" if hour%24<12 else "PM"
    minute = minute%60
    hour = hour%12
    hour = 12 if hour==0 else hour
    new_time = '%d:%02d %s%s%s'%(hour,minute,time,week,day)
    return new_time