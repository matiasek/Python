def IsPrime(num):
    counter=0
    for i in range(1,num+1):
        if num%i==0:
            counter+=1
    if counter > 2:
        return False
    else:
        return True
            
print("Liczby pierwsze to")
for i in range(1,200):
	if IsPrime(i+1)==True:
			print(i+1,end=" ")
print()