import sys

smin = 60
shour = 3600
sday = 86400
sweek = 604800
smonth = 2419200
syear = 29030400
t = [0,0,0,0,0,0,0]

def convert(s, tm=t):
    print("s is %i"%s)
    if s >= syear:
        print("%i greater than a year"%s)
        sy = s//syear
        s = s%syear
        t[0] = sy
    elif s >= smonth:
        print("%i greater than a month"%s)
        sm = s//smonth
        s = s%smonth
        t[1] = sm
    elif s >= sweek:
        print("%i greater than a week"%s)
        sw = s//sweek
        s = s%sweek
        t[2] = sw
    elif s >= sday:
        print("%i greater than a day"%s)
        sd = s//sday
        s = s%sday
        t[3] = sd
    elif s >= shour:
        print("%i greater than an hour"%s)
        sh = s//shour
        s = s%shour
        t[4] = sh
    elif s >= smin:
        print("%i greater than a minute"%s)
        smi = s//smin
        s = s%smin
        t[5] = smi
    elif s >= 1:
        ss = s
        s = 0
        t[6] = ss
    elif s < 1:
        print("%i smaller than a second"%s)
        pass
    
    if s >= 1:
       convert(s,t)

    return t
    print("convert exiting")

b = 0
while (b is 0):
    try:
        sec = int(input("Enter seconds to be converted (ms will be removed) "))
        b = 1
    except NameError:
        print("Please enter a valid number.")
        b = 0

print("%i entered"%sec)

tm = convert(sec)

print("%i years, %i months, %i weeks, %i days, %i hours, %i minutes and %i seconds"%(tm[0],tm[1],tm[2],tm[3],tm[4],tm[5],tm[6]))
