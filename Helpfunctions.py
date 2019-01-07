import unittest
import itertools as it


def help_islice(iterable, args):
   
    return list(it.islice(iterable,args))

def help_islice_2(iterable, start, stop):
   
    return list(it.islice(iterable,start,stop))


def help_islice_3(iterable, start, stop, step):
    
    return list(it.islice(iterable,start,stop, step))

## Helpfunction for count to make the function itertools.count stop counting after a given amount of steps
def count_stop(start,step,stop):
    items = []
    for i, item in enumerate(it.count(start,step)):
        items.append(item)
        if i == stop:
            break
    return items
