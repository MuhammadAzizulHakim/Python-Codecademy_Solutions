#version1:
def median(x):
    xsort = sorted(x)
    if len(xsort) % 2 == 0:
        right = len(xsort) / 2
        left = (len(xsort) / 2) - 1
        return (xsort[right] + xsort[left]) / 2.0
    else:
        return xsort[len(xsort) / 2]
        
print median([1,3,6,7,0,2,90,8])


#version2:
def median(x):
    l = sorted(x)
    if len(l) % 2 == 0:
        return (l[len(l) / 2] + l[(len(l) / 2 ) - 1]) / 2.0
    else:
        return l[len(l) / 2]
        
print median([1,3,6,7,0,2,90,8])
