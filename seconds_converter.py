import sys

smin = 60
shour = 3600
sday = 86400
sweek = 604800
smonth = 2419200
syear = 29030400
t = [0, 0, 0, 0, 0, 0, 0]


def convert(s, tm=t):
    if s >= syear:
        sy = s//syear
        s = s % syear
        t[0] = sy
    elif s >= smonth:
        sm = s//smonth
        s = s % smonth
        t[1] = sm
    elif s >= sweek:
        sw = s//sweek
        s = s % sweek
        t[2] = sw
    elif s >= sday:
        sd = s//sday
        s = s % sday
        t[3] = sd
    elif s >= shour:
        sh = s//shour
        s = s % shour
        t[4] = sh
    elif s >= smin:
        smi = s//smin
        s = s % smin
        t[5] = smi
    elif s >= 1:
        ss = s
        s = 0
        t[6] = ss
    elif s < 1:
        pass

    if s >= 1:
       convert(s, t)

    return t


def format_ans(tm=[0, 0, 0, 0, 0, 0, 0]):
    answer = "Answer is "
    ay = "" if tm[0] is 0 else " % i year(s), " % tm[0]
    am = "" if tm[1] is 0 else " % i month(s), " % tm[1]
    aw = "" if tm[2] is 0 else " % i week(s), " % tm[2]
    ad = "" if tm[3] is 0 else " % i day(s), " % tm[3]
    ah = "" if tm[4] is 0 else " % i hour(s), " % tm[4]
    ami = "" if tm[5] is 0 else " % i minute(s), " % tm[5]
    ase = "%i second(s)." % tm[6]
    answer = answer+ay+am+aw+ad+ah+ami+ase
    
    return answer


b = 0
while (b is 0):
    try:
        sec = int(input("Enter seconds to be converted (ms will be removed) "))
        b = 1
    except NameError:
        print("Please enter a valid number.")
        b = 0
    except ValueError:
        print("Please enter a valid decimal number.")

        b = 0
if sec < 0:
    sec = abs(sec)
    print("Negative number detected, using absolute value.")

print("Converting %i'' to readable form." % sec)

tm = convert(sec)
answer = format_ans(tm)

print(answer)
