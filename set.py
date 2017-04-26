A = [1,2,3]
B = [3,4,5]

def union(set1,set2):
    return set1 + [x for x in set2 if (x not in set1)]

def intersect(set1,set2):
    return [x for x in set2 if (x in set1)]

def setDiff(set1,set2):
    return [x for x in set1 if (x not in set2)]

def symDiff(set1,set2):
    return [x for x in union(set1,set2) if (x not in intersect(set1,set2))] 

def cartesianProduct(set1,set2):
	return [(x,y) for x in set1 for y in set2]

print union(A,B)
print intersect(A,B)
print setDiff(A,B)
print symDiff(A,B)
print cartesianProduct(A,B)