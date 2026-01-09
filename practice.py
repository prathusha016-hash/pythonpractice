#input and output,string manipulation and comment

#simple greeting program

'''
#
name=input("enter the name:")
age=int(input("enter the age :"))
print("hello! "+ name + " you are " + str(age) + " years old ")'''
#string manipulation exercise
'''
sentence=input("enter the sentence:")
print(sentence.upper())
print(sentence.lower())
print(sentence.replace(" ","_"))
print(sentence.strip())'''
#character counter
'''
text=input("enter the text:")
count=len(text.replace(" ",""))
print("number of char in the given text:",count)'''
#escape sequence practice
'''
print("hello\n\tworld")
print("this is a back slash:/")'''

#opertors homework
'''
a=int(input("enter the number:"))
b=int(input("entr the number:"))
print("both are greater than 10:",a>10 and b>10) 
print("atleat one is less than 5:",a<5 or b<5)
print("first number is not greater than second:",not(a>b))'''
'''
age=int(input("enter your age:"))
if age>=18:
    print("you are an adult")
else:
    print("you are minor") '''   
#another method
'''
age = int(input("Enter your age: "))

print(age >= 18 and "You are an adult" or "You are a minor")
'''

#membership operator
'''
string=input("enter the string:")
print('a' in string)
print('python' not in string)'''

#bitwise operator
'''
a=int(input("enter the number:"))
b=int(input("enter the second number:"))
print(a&b)
print(a|b)
print(a^b)
print(a<<2)
print(b>>1)'''

#lists

#list manipulation exercise:
''' 
my_list=[10,20,30,40,50]
print("original list:",my_list)

my_list.append(60)
print("after appending:",my_list)

my_list.insert(1,15)
print("aftre inserting:",my_list)

my_list.pop(2)
print("after removing the third element:",my_list)

my_list[5]=70
print("after replacing 60:",my_list)'''

#in list we cant use replace keyword 
#by index position we can replace

#reversing and sorting the list

"""number=[5,8,2,5,7,1]

number.sort(reverse=True)# sort in descending order 
print("sorted in descending order:",number)

#reverse the sorted list
number.reverse()
print("reversed list:",number)"""

