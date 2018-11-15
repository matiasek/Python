'''

Your task is to write and test a function which takes two arguments (a year and a month) 
and returns the number of days for the given month/year pair 
(while only February is sensitive to the year value, your function should be universal). 
The initial part of the function is ready. Now, convince the function to return None if its arguments don't make sense.
31 - 1,3,5,7,8,10,12
30 - 2,4,6,9,11
Of course, you can (and should) use the previously written and tested function.
It may be very helpful. We encourage you to use a list filled with the months' lengths. 
You can create it inside the function - this trick will significantly shorten the code.
jesli przestepny to luty ma 29 dni
We've prepared a testing code. Expand it to include more test cases.
'''
import math
def IsYearLeap(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        return True
    else:
        return False

def DaysInMonth(year,month):
    if isinstance(year,int)==True and isinstance(month,int)==True:
        print("To jest liczba")
        if month==2:
            if IsYearLeap(year)==True:
                print(year,"jest przestepny",end=" ")
                return 29
            else:
                print(year,"nie jest przestepny",end=" ")
                return 28
        else:
            if month%2==0 or month==9 or month==11:
                return 30
            else:
                return 31
    else:
        print("To nie jest liczba")
        return None;

testyears = [1900, 2000, 2016, 1987]
testmonths = [ 2, 'x', 1, 11]
testresults = [28, 29, 31, 30]
for i in range(len(testyears)):
	yr = testyears[i]
	mo = testmonths[i]
	print(yr,mo,"->",end="")
	result = DaysInMonth(yr,mo)
	print("Funkcja zwrocila:",result,end=" ")
	if result == testresults[i]:
		print("OK")
	else:
		print("Failed")
		
		
		
		
