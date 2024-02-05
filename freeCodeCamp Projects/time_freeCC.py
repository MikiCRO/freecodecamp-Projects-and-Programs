def add_time(start, duration,day_week=""):
    week = ["Monday", "tuesday", "Wednesday", "Thursday", "Friday", "saturDay", "Sunday"]
    start_t,ampm_s=start.split(" ")
    starting_h,starting_m=start_t.split(":")
    duration_h,duration_m=duration.split(":")
    days = 0
    ampm_new=ampm_s
    
    new_h= int(starting_h) + int(duration_h)
    new_m = int(starting_m) + int (duration_m)
    
    while new_m >= 60:
        new_m -= 60
        new_h += 1
    
    new_m = "%02d" % new_m
    
    while new_h >= 24:
        new_h -= 24
        days += 1
    
    
    if int(starting_h) < 12 and new_h >= 12:
       
        if ampm_s == 'AM':
            ampm_new = 'PM'
            
        elif ampm_s == 'PM':
            ampm_new = 'AM'
            days += 1
    if new_h > 12:
        new_h -= 12
    
    new_time = ":".join((str(new_h), str(new_m)))
    new_time += " " + ampm_new
    
    
    if day_week != "":
        for k,v in enumerate(week):
            if day_week == v:
                k =(k + days) %7
                if days == 1:
                    zagrade = '(next day)'
                    new_time +=", "+week[k] + " " + zagrade
                    return new_time
                    
                elif days > 1:
                    zagrade = f'({days} days later)'
                    new_time +=", "+week[k] + " " + zagrade
                    return new_time
                elif days == 0:
                    new_time +=", "+week[k]
                    return new_time
                    
    if days == 1:
        zagrade = '(next day)'
        new_time += " " + zagrade
        
    elif days > 1:
        zagrade = f'({days} days later)'
        new_time +=" " + zagrade
    
    return new_time
    
#print(add_time("11:55 AM", "3:12"))
    
    
    
    
                    
            
            
            
