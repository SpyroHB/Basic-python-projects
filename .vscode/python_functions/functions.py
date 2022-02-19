import datetime
def date_time(day,month,year):
    now = datetime.datetime.now()
    x = now.strftime("%d")
    y= now.strftime("%m")
    z = now.strftime("%Y")
    
    print(f"{x}-{y}-{z}")

date_time()


