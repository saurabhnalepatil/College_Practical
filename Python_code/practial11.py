

'''

#creating module and saving it by name mymodule.py
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

def add(a,b):
    return a+b
    
'''


#importing our module we save as mymodule.py
import mymodule

#using module person1 object
a = mymodule.person1["name"]
print(a)
a = mymodule.person1["country"]
print(a)
a = mymodule.person1["age"]
print(a)

a=mymodule.add(10,20)
print(a)


#using importlib to reload module if module change in between program 
import importlib

import mymodule
#This code got executed

import mymodule

#reloading module using importlib module
importlib.reload(mymodule)
