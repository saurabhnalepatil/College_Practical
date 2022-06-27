#try/except/else statement
def divide(x,y):
    try:
        result=x//y
    except ZeroDivisionError:
        print("Sorry! you are dividing by zero")
    else:
        print("Yeah ! Your answer is :",result)
        
divide(4,2)
divide(4,0)
******************OUTPUT**************
Yeah ! Your answer is : 2
Sorry! you are dividing by zero
-------------------------------------------
#try/finally Statement
try:
    fh=open("testfile","t")
    fh.write("This is my file for exceptions handlling!!")
finally:
    print("Error:can't find file or read data")
******************OUTPUT**************
Error:can't find file or read data
----------------------------------------------
#unified try/except/finally
def divide(x,y):
    try:
        result=x//y
    except ZeroDivisionError:
        print("Sorry! you are dividing by zero")
    else:
        print("Yeah ! Your answer is :",result)
    finally:
         print("this is always executed")
divide(4,5)
divide(4,0)
******************OUTPUT**************
Yeah ! Your answer is : 0
this is always executed
Sorry! you are dividing by zero
this is always executed
--------------------------------------------------
#Raise Statement
a=int(input())
b=int(input())

try:
    if a<0 or b<0:
        raise ZeroDivisionError
    print(a/b)
except ZeroDivisionError:
        print("plese enter valid  integer number")
******************OUTPUT**************

2
52
0.038461538461538464
2
0
plese enter valid  integer number
----------------------------------------------------
#Assert StAtement
a=int(input())
b=int(input())
#using assert to check for 0
print("The value of a/b is:")
assert b!=6,"Zero Division Error"
print(a/b)
******************OUTPUT**************
5
4
The value of a/b is:
1.25
---------------------------------------------------
#catch multiple specific exceptions
import sys
randomList=['a',0,2]
for entry in randomList:
    try:
        print("The entry is",entry)
        r=1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occurred.")
        print("Next entry.")
        print()
print("The reciprocal of",entry,'is',r)
******************OUTPUT**************

The entry is a
Oops! <class 'ValueError'> occurred.
Next entry.

The entry is 0
Oops! <class 'ZeroDivisionError'> occurred.
Next entry.

The entry is 2
The reciprocal of 2 is 0.5
