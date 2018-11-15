'''Your task is to write a function checking whether a number is prime or not.

The function:

is called IsPrime;
takes one argument (the value to check)
returns True if the argument is a prime number, and False otherwise.
Hint: try to divide the argument by all subsequent values (starting from 2) and check the remainder - if it's zero, your number cannot be a prime; think carefully about when you should stop the process.

If you need to know the square root of any value you can utilize the ** operator. Remember: the square root of x is the same as x0.5

Complete the code presented below.

Run your code and check whether your output is the same as ours.

2 3 5 7 11 13 17 19 '''

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
