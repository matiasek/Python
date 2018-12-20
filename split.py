def mysplit(strng):
    lst = [None] * (strng.count(" ")+1)
    for i in range(len(lst)):
        x= 0 if i==0 else (strng.find(" ",x+1)+1)
        lst[i]=strng[x:len(strng) if i==(len(lst)-1) else strng.find(" ",x+1)]
    return lst

print(mysplit("To be or not hello whateverfor you"))
'''test
iterations
lst[0]=strng[0:2]
lst[1]=strng[3:5]
lst[2]=strng[6:8]
lst[3]=strng[9:12]

'''
