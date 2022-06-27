practicle:-9. Demonstrate implementation of the-
               - Anonymous Function Lambda.
----------------------------------------------------------
sum=(lambda x,y:x+y)
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print("sum =",sum(a,b))
minus=(lambda x,y:x-y)
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print("minus =",minus(a,b))
mult=(lambda x,y:x*y)
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print("mul =",mult(a,b))
div=(lambda x,y:x/y)
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print("div =",div(a,b))
mod=(lambda x,y:x%y)
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print("mod =",mod(a,b))
*******************OUTPUT********************************
Enter the value of a:5
Enter the value of b:5
sum = 10
Enter the value of a:2
Enter the value of b:5
minus = -3
Enter the value of a:225
Enter the value of b:5
mul = 1125
Enter the value of a:15
Enter the value of b:6
div = 2.5
Enter the value of a:2
Enter the value of b:5
mod = 2
----------------------------------------------------------
def a_first(a):
    return a[1]
a = [[1,4],[5,6],[3,5]]
a.sort(key = a_first)
print(a)
*********************OUTPUT********************************
[[1, 4], [3, 5], [5, 6]]
--------*****-----------******-----------------------------
def sum(a,b):
    return a+b
print(sum(5,5))
def sub(c,d):
    return c-d
print(sub(5,6))
def mul(x,y):
    return x*y
print(mul(5,5))
def a_first(a):
    return a[1]
a = [[1,4],[5,6],[3,5]]
a.sort(key = a_first)
print(a)
*********************OUTPUT*********************************
10
-1
25
[[1, 4], [3, 5], [5, 6]]
