import datetime
# Current Date in dd/mm/yyyy
def date_timeNow():
    now = datetime.datetime.now()
    x = now.strftime("%d")
    y= now.strftime("%m")
    z = now.strftime("%Y")
    
    print(f"{x}-{y}-{z}")
