# the following code was used to solve a geocache puzzle.
# Maidenhead coordinates were given (via morse code), but the online
# converters take 6 characters (3 pairs) which is sufficient for
# ham radio operators to give their location within half a square km
# but not sufficient for a geocace. I couldn't find any online tool that
# went further so I wrote this instead. Probably not optimized

from numpy import array, modf
from math import trunc


first_pair = dict(zip(list('ABCDEFGHIJKLMNOPQR'),range(0,18)))
next_pair = dict(zip(list('ABCDEFGHIJKLMNOPQRSTUVWX'),range(0,24)))

instring = "QF22LE60SF88"

def convert_to_gps(instring):
    instring = instring.upper()
    size = len(instring)//2
    pairs = [instring[2*i:2*i+2] for i in range(size)] 
    long = 0
    lat = 0
    for i,pair in enumerate(pairs):
        if i == 0:
            long += first_pair[pair[0]]*20 - 180 # 0 is at antimeridian of Greenwich
            lat += first_pair[pair[1]]*10 - 90 # 0 is at south pole
            prev = array([20,10]) # previous division in degrees
        else:
            if pair.isnumeric():
                long += int(pair[0])*prev[0]/10
                lat += int(pair[1])*prev[1]/10
                prev = prev/10
            else:
                long += next_pair[pair[0]]*prev[0]/24
                lat += next_pair[pair[1]]*prev[1]/24
                prev = prev/24

    long += .5*prev[0] # move to center
    lat += .5*prev[1] # move to center



    return lat,long
    



def degree_format(coords):
    lat = coords[0]
    long = coords[1]
    degrees = array([lat,long])
    # DOES NOT WORK: gives pos conjugate (minutes = (degrees%1)*60)
    minutes = modf(degrees)[0]*60
    prefix = ["E","N"]
    if lat < 0:
        prefix[1] = "S"
    if long < 0:
        prefix[0] = "W"
    # make positive for final printout/return
    degrees = abs(degrees)
    minutes = abs(minutes)
    long_return = f'{prefix[0]} {trunc(degrees[0])}° {minutes[0]:,.3f}'
    lat_return = f'{prefix[1]} {trunc(degrees[1])}° {minutes[1]:,.3f}'
    return f'{lat_return}\n{long_return}'




#lat,long = convert_to_gps(instring)
#print(lat,long)
coords = degree_format(convert_to_gps(instring))
print(coords)
