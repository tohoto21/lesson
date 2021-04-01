#import  time


#start = time.time()
l=[1,2,3,4,5,6,7,8,9]
#print(list(zip(*([iter(l)]*3))))
print(list(zip(*zip(l))))
#print([(l[i], l[i+ 1], l[i+ 2]) for i in range(0, len(l), 3) if i != (len(l) - 2)])
#print(list((l[i-2],l[i-1],l[i])for i in range(2,len(l),3)))
#end = time.time()
#print(end - start)