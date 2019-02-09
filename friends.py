def mean_num_friends(x):
    count=0
    for f in x: count+=f
    return (count/len(x))

def median_num_friends(x):
    sortedX=sorted(x)
    if(len(sortedX)%2!=0): return sortedX[(len(sortedX)//2)]
    return (sortedX[(len(sortedX)//2)]+sortedX[(len(sortedX)//2)-1])/2

num_friends=[100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]
print("mean={}".format(mean_num_friends(num_friends)))
print("median={}".format(median_num_friends(num_friends)))