#version1:
def count(sequence,item):
    return sequence.count(item)

print count([1,2,3,2,1],1)


#version2:
def count(sequence, item):
    found = 0
    for i in sequence:
        if i == item:
            found +=1
    return found

print count([1,2,3,2,1],1)
