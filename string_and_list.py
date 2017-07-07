words = "It's thanksgiving day. It's my birthday,too!"
string=words.replace(" day"," month")
print string

x = [2,54,-2,7,12,98]
print "Min is "+ str(min(x))
print "Max is "+ str(max(x))

y = ["hello",2,54,-2,7,12,98,"world"]
z=[y[0],y[len(y)-1]]
print z

num = [19,2,54,-2,7,12,98,32,10,-3,6]
num.sort()
print num
list1=num[:len(num)/2]
list2=num[len(num)/2:]
list2.insert(0,list1)
print list2
