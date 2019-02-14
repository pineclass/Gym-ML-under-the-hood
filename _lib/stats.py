from collections import Counter
import math
import numpy as np

def mean(x):
    return sum(x) / len(x)

def median(x):
    x_s = sorted(x)
    l = len(x)
    mid_p = l//2

    if l % 2 == 1:
        return x_s[ mid_p ]
    else:
        return ( x_s[ mid_p -1 ] + x_s[ mid_p ] ) / 2

def quantile( x, p ):
    p_index = int( p * len(x) )
    return sorted( x )[p_index]


##

def deviation( x ):
    x_bar = mean( x )
    return [ x_i - x_bar for x_i in x ]

def variance( x ):
    n = len( x )
    dev = deviation( x )
    return sum( [ d**2 for d in dev  ] ) / ( n - 1 )

def standard_deviation( x ):
    return math.sqrt( variance( x ) )

##

def covariance( x, y ):
    n = len( x )
    return np.dot( deviation(x), deviation(y) ) / ( n - 1 )

def correlation( x, y ):
    stdev_x = standard_deviation( x )
    stdev_y = standard_deviation( y )
    if stdev_x * stdev_y == 0 : return 0
    else: return covariance(x, y) / stdev_x / stdev_y

