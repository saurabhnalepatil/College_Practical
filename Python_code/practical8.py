Practicle no:-8
Demonstrate the concept of String-Based Exceptions, Class-Based Exceptions and Nesting 
Exception handlers. 
-------------------------------------------------------------------
#String-based exception
try:
    num_list=[10]
    num_list+=5
except Exception as error:
    error_string=str(error)
    print(error_string)
    print("\n")
**************OUTPUT***************************          
'int' object is not iterable
----------------------------------------------------------------
#Class-based Exception
class Error(Exception):
    pass
class ValueTooSmallError(Error):
    pass
class ValueTooLargeError(Error):
    pass
#you need to guess this number
number=int(input("enter number"))
#user gusses a number until he/she gets it right
while True:
    try:
        i_num=int(input("enter  a number:"))
        if i_num<number:
            raise ValueTooSmallError
        elif i_num>number:
             raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This Value is too Small,try again!")
        print()
    except ValueTooLargeError:
        print("This Value is too Large,try again!")
        print()
print("Congratulations! you guessed it correctly.")
print("\n")
****************OUTPUT**********************
enter number50
enter  a number:41
This Value is too Small,try again!
enter  a number:51
This Value is too Large,try again!
enter  a number:50
Congratulations! you guessed it correctly.
----------------------------------------------------------
#Nested Exception Handlers
def divide(x,y):
    try:
        print(f'{x}/{y}is {x/y}')
    except ZeroDivisionError as e:
        print(e)
    else:
        print("divide() function worked fine.")
    finally:
        print("close all the resources here")
divide(50,15)
divide(50,0)
divide(50,4)
*****************OUTPUT*******************
50/15is 3.3333333333333335
divide() function worked fine.
close all the resources here
division by zero
close all the resources here
50/4is 12.5
divide() function worked fine.
close all the resources here
