from collections import defaultdict
from collections import Counter
import numpy as np
def median(mylist):
    sorts = sorted(mylist)
    length = len(sorts)
    if not length % 2:
        return (sorts[length / 2] + sorts[length / 2 - 1]) / 2.0
    return sorts[length / 2]


def avg(sequence):
        if len(sequence) < 1: 
            return None
        else: 
            return sum(sequence) / len(sequence)   

def variance(sequence):
    def avg(sequence):
        if len(sequence) < 1: 
            return None
        else: 
            return sum(sequence) / len(sequence)   

    if len(sequence) < 1: 
        return None
    else:
        avg = avg(sequence)
        sdsq = sum([(i - avg) ** 2 for i in sequence])
        stdev = (sdsq / (len(sequence) - 1)) ** .5
        return stdev
        

#percentile is a real number (0,100)    
def percentile (sequence, percentile):
    if len(sequence) < 1: 
        value = None
    elif (percentile >= 100):
        sys.stderr.write('ERROR: percentile must be < 100.  you supplied: %s\n'% percentile)
        value = None
    else:
        element_idx = int(len(sequence) * (percentile / 100.0))
        sequence.sort()
        value = sequence[element_idx]
        return value

def mode(ls):
    a= list(map((lambda x: x * -1), ls))
    counts=np.bincount(a)
    return  -1* np.argmax(counts)
    '''
    b = Counter(ls)
    return b.most_common(1)
    max=-1
    modes =defaultdict(dict)

    for i in ls:
        modes[i]=ls.count(i)
    for i,k in modes.iteritems():
        if k >max :
            max=k
    for i,k in modes.iteritems():
        if k==max:
            return i
        '''
import pytz, datetime, time
# prints e.g. 2010-03-31 13:01:18
def timeStamp_Conversion(start_time,end_time,router_id):
#format of string :"2013-08-29 19:58:04.199154"
    start_o=datetime.datetime.strptime(start_time,"%Y-%m-%d %H:%M:%S")
    UTC_start_timestamp=time.mktime(start_o.timetuple())

    end_o=datetime.datetime.strptime(end_time,"%Y-%m-%d %H:%M:%S")
    UTC_end_timestamp=time.mktime(end_o.timetuple())

    #print "original:",datetime.datetime.fromtimestamp(UTC_timestamp)
    table={
        'OWC43DC7B0AE69' :"US/Eastern",
        'OWC43DC7A3EE22' :"US/Eastern",
        'OWC43DC78EE081' :"US/Pacific",
        'OWC43DC7A3EE3A' :"US/Pacific",
        }
    # re-interpret 
    originalTimeZone = table[router_id]
    targetTimeZone   =  "UTC"

    new_start_timestamp = pytz.timezone(originalTimeZone).localize(datetime.datetime.fromtimestamp(UTC_start_timestamp)).astimezone(pytz.timezone(targetTimeZone))

    new_end_timestamp = pytz.timezone(originalTimeZone).localize(datetime.datetime.fromtimestamp(UTC_end_timestamp)).astimezone(pytz.timezone(targetTimeZone))
    # prints e.g. 2010-03-31 22:01:18+02:00
    local_start_timestamp = time.mktime(new_start_timestamp.timetuple())
    local_end_timestamp = time.mktime(new_end_timestamp.timetuple())
    # print time difference in hours
    '''
    print (local_start_timestamp - UTC_start_timestamp) / 3600.0
    print (local_end_timestamp - UTC_end_timestamp) / 3600.0
    print (local_end_timestamp-local_start_timestamp)/3600.0
    print (UTC_end_timestamp-UTC_start_timestamp)/3600.0
    '''
    return [local_start_timestamp,local_end_timestamp]

