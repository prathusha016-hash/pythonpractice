'''file=open("notes.txt","r")
#content=file.read()
print(file)
file.close()'''


'''students=["darshan","chandhan","przthusha"]

with open("example.txt","w") as file:
    for student in students:
        file.write(f"{student}\n")
        print("file created" )'''

'''import my_library.greeting as greetings# my_library inside that greetings inside that namaskara is one of the method defined
#or
from my_library import greetings

greetings.namaskara("meena")

#or

from my_library.greetings import namaskara # directly taking it
namaskara("meena")
#or

from my_library.greetings import namaskara as nm
nm('meena')'''

#you can find all this in pypi.org and install using pip install module_name


#to import the wikipedia module we have to install it first using pip install wikipedia
'''import wikipedia # pip install wikipedia
print(wikipedia.summary("anushka shetty"))'''

#to currency converter
'''from currency_converter import currencyconverter # pip install currency_converter
c=currencyconverter()
amt=float(input("enter the amt in USD: "))
NEW_AMT=c.convert(amt,'USD','INR')
print(f"amt in inr:{NEW_AMT}")
'''
'''

from currency_converter import CurrencyConverter  # pip install currency_converter

# create an instance of CurrencyConverter
c = CurrencyConverter()

# take input in USD
amt = float(input("Enter the amount in USD: "))

# convert to INR
NEW_AMT = c.convert(amt, 'USD', 'INR')

print(f"Amount in INR: {NEW_AMT}")'''


#to generate qr code.....

'''import qrcode # pip install qrcode

image=qrcode.make("engineeringinkannada.com")
image.save("my_qr_code.png")
print("qrcode generated successfully")'''

#also we can generate qr code according to color and amny more you can check out in pypi.org

#For more control, use the QRCode class. For example:
'''
import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="white")
img.save("colour_qr_code.png")'''

#match case in python

'''num=int(input("enter the number:"))

match num:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case _:
        print("number is not in the range of 1 to 3")   '''

#decorators

#returning function has parameters
'''
def f():
    print("hello")
    def a():
        print("welcome to python")
    return a 
l=[f]
l[0]()'''

#@decorate syntax
'''
def decorator_name(func):
    def wrapper():
        print("namaskara")
        func()

        print("take care!")
    return wrapper
    
@decorator_name    
def intro():
    print("im from karnataka") 

intro()
'''
#logging using decorators

'''def show_result(func):
    def wrapper(a,b):
        print(f"function '{func.__name__}' is being called")
        func(a,b)
    return wrapper

@show_result
def add(a,b):
    print(a+b)   

@show_result
def sub(a,b):
    print(a-b)     
    
add(5,3)   
sub(5,3) '''

#map function
'''
nums=[1,2,3,4]
def double(x):
    return x*2
res=map(double,nums)#syntax : map(function,iterable)
print(list(res))

#another method using lambda function 

nums=[1,2,3,4]
res=map(lambda x:x*3,nums)
print(list(res))

#multiple mapping

a=[1,2,3]
b=[4,5,6]
res=map(lambda x,y:x+y,a,b)
print(list(res))'''

#filter function
'''
nums=[1,2,3,4,]
def is_even(x):
    return x%2==0
res=filter(is_even,nums) #synrax: filter(function,iterable)
print(list(res))

#using lambda function

nums=[1,2,3,4,]

res=filter(lambda x:x%2==0,nums) 
print(list(res))'''

#reduce function
'''
from functools import reduce
nums=[1,2,3,4]
def add(x,y):
    return x+y
res=reduce(add,nums)
print(res)

#product of numbers using reduce function
from functools import reduce
nums=[1,2,3,4]

res=reduce(lambda x,y:x*y,nums)
print(res)

#to find maximum value using reduce function

from functools import reduce
nums=[1,5,100,45]
res=reduce(lambda x,y:x if x>y else y,nums)
print(res)'''

#example program of filter,mapping, and reduce function
'''from functools import reduce
scores=[80,90,75,60,85]

#updating scores by adding 5 bonus marks using map function
updated_scores=list(map(lambda x:x+5,scores))
print("updated_scores:", updated_scores)
#filtering out scores greater than 85 using filter function
passed=list(filter(lambda x:x>85,updated_scores))
print("filtered_scores:",passed)
#finding total of all students
total=reduce(lambda x,y:x+y,passed)
print("total of all students:",total)'''

#iterator

'''numbers=[1,2,3]
it=iter(numbers)
print(next(it))
print(next(it))
print(next(it))
#print(next(it))#raise stopiteration error because there is no more element to iterate

#using iterators using loops

nums=[10,20,30]
for num in nums:
    print(num)#internally it uses iteration'''

#custom iterator
'''class countdown:
    def __init__(self,start):
        self.start=start
    def __iter__(self):
        return self
    def __next__(self):
        if self.start<=0:
            raise StopIteration
        
        num=self.start
        self.start-=1
        return num
cd= countdown(5)
for i in cd:
    print(i)
'''

#generator function
#generator is an easier way of creating iterators using yield keyword

'''def simple_gen():
    yield 1
    yield 2
    yield 3
for i in simple_gen():
    print(i)

def simple_gen():
    yield 1
    yield 2
    yield 3
g= simple_gen()   
for i in g:
    print(i)'''
    
'''def simple_gen():
    yield 1
    yield 2
    yield 3
g= simple_gen()   
print(next(g))
print(next(g))
print(next(g))'''

#generators another example
'''def f(x):
    yield x*2
g=f(5)
for i in g:
    print(i)'''
#another way 

'''def simple_gen(x):
    for i in range(x):
        yield i
    
g= simple_gen(5)   
for i in g:
    print(i)

'''
#single line generators cld generator expressions
'''
import sys #to check the size of the object in the memory

l=[x*x for x in range(5)]#here we are using square bractes to create list 
print(l)
print(type(l))
print(sys.getsizeof(l))

dl=(x*x for i in range(5))#here we are using round bractes to create generator expression
print(dl)
print(type(dl))
print(sys.getsizeof(dl))'''

#infinite generator

def infinite_numbers():
    num = 1
    while True:
        yield num
        num += 1

gen = infinite_numbers()
for i in range(5):
    print(next(gen))

    







    








