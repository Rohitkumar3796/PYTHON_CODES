# HOW CAN WE CONVERT STRING VALUE TO INT
str1="Hello World!"
int_=''.join(map(str,map(ord,str1)))
print(int(int_))
# --------------------------------------------------------------------
txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 3) #here 3 means how much time "one is repeated in the string"
print(x)
# ------------------------------------------------
a,b=(input("enter")).split()#here i se split function to split input
print(int(a)+int(b))
# -----------------------------------------------------------------------------
# from tkinter import *
# from tkinter.ttk import *
# from time import strftime
# root=Tk()
# root.title("Clock")
# def time():
#     string=strftime('%H:%M:%S %p')
#     label.config(text=string)
#     label.after(1000,time)
#
# label=Label(root,font=("ARIAL" ,20),bg="GREY",fg="WHITE")
# label.pack(anchor="center")
# time()
# root.mainloop()
# =================================================================
string="one two three\nfour\tfive" #\n and \t means space so split function is used to split from space
print(string.split())
# ------------------------------
string="one,two,three,four,five" #here i separated the string from comma and use spllit function and
#number also so it splits the 3 starting string separated by string and left of the string is printed in a single string separated by comma
print(string.split(",",3))
# ----------------------------------------------------
string="one\ntwo\nthree\nfour"
print(string.split('\n',2)[2]) #it print like nested list of string here i use slicing from different type
# --------------------------------------------------
s="one,two,three,four" #here we can also split from right side
print(s.rsplit(',',2)[-1])
# ---------------------------------------------------
s_lines_multi = '1 one\n2 two\r\n3 three\n'
print(s_lines_multi.split()) #['1', 'one', '2', 'two', '3', 'three']
print(s_lines_multi.split("\n"))#['1 one', '2 two\r', '3 three', '']
print(s_lines_multi.splitlines())#['1 one', '2 two', '3 three'](splits at various newline characters but not at other whitespace.not include)
# ------------------------------------------------------------------------------
# string="rrrrohit"
# a=string.lower()
# b=input("char")
# v=a.count(b)
# for i in range(v):
#     a=a.replace(b,'*')
# print(a.capitalize())
# ----------------------------------------------
# list_of_numbers=list(range(10))
# print(list_of_numbers)
# ------------------------------------------/
# list=[1,2,3,4,5,13,7,8]
# print(list[list[4]]) #here list of index of 4, the value is 5 but another list 0f 5 as a index number for another list so it prints 13, index of
# ----------------------------------------------------
# list=[]
# for i in range(4):
#     if len(list)==i:
#         list.insert(i,int(input('num')))
# print(list)
# ------------------------------------
# squares and sum of natural number
n=int(input("num"))
m=0
for i in range(1,n+1):
    a=i**2
    print(a)
    m=a+m
print(m)
# ------------------------------------------------------------
# recursive fuction to calculate sum of square of natural numbers
def sq_num(n):
    if n==1:
        return n
    else:
        r=sq_num(n-1)
        return r+n**2
n=int(input("number"))
print(sq_num(n))
# ---------------------------------
# use return keyword omly to return the value
def print_nums(x):
  for i in range(x):
    print(i)
    return
print_nums(10)
# ------------------------------------
# Celsius = (Fahrenheit – 32) * 5/9
# Fahrenheit = (Celsius * 9/5) + 32
celsius = int(input())
def conv(c):
    return (c * 9 / 5) + 32

fahrenheit = conv(celsius)
print(fahrenheit)
# ---------------------------------------------
# nums = {1, 2, 3, 4, 5, 6}
# nums = {0, 1, 2, 3} & nums #here i use and oerator, so it's comparing the value in both sets
#
# nums = filter(lambda x: x > 1, nums)
# print(len(list(nums)))
# --------------------------------------------------
foo=print()
if foo==None:
    print(1)
else:
    print(2)
# ------------------------------------------------
# def deliver(houses):
#     if len(houses) == 1:
#         house = houses[0]
#         print("DELIVER", house)
#     else:
#         res = len(houses) // 2
#         first_half = houses[:res]
#         second_half = houses[res:]
#         return first_half, second_half
#
# print(deliver(["Eric's houses", "Rohit houses", "Amit houses", "Pooja houses"]))
# ----------------------------------------------------------------------------------
def fun(func,arg):
    return func(func(arg))

def mult(x):
    return x+x

v=fun(mult,3) #what happened here when will pass mult function to fun function as an argument in func parameter
print(v) #In second line of fun function there is return so there we call mult fucntion and pass value args as a value to mult function
# -----------------------------------------------------------------
# PRIME OR NOT
n=30
for i in range(2,n):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i,'prime')
# ==========================================
# def power(x, y):
#     if y == 0:
#         return 1
#     else:
#         return x * power(x, y - 1)
#
# print(power(2, 3))=
# ---------------------------------------------
# from itertools import accumulate, takewhile
#
# nums = list(accumulate(range(8)))
# print(nums)
# print(list(takewhile(lambda x: x<= 6, nums)))

# -----------------------------------------------
# def fib(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         fibo= fib(n-1) +fib(n-2)
#         return fibo
# print(fib(int(input('num'))))
#
# ---------------------------------------
# from functools import reduce
# number=[1,2,3,4,5]
# sum of list of numbers by reduce function
# c=reduce(lambda x,y:x+y,number)
# print(c)
# ----------------------------------------------
# import re
# c=re.findall(r'\w','http://www.hackerrank.com/')
# print(c)
#
# c=re.finditer(r'\w','http://www.hackerrank.com/')
#
# v=list(map(lambda x: x.group(),c))
# print(v)
#
# string="rabcdeefgyYhFjkIoomnpOeorteeeeet"
# -------------------------------------------------------------
# nums=[1,2,3,4,5,6,7]
# res=list(filter(lambda x:x%2==0,nums))
# print(res)
# ------------------------------------------
# def spell(txt):
#     if txt=="":
#         return txt
#     else:
#         a=spell(txt[1:])
#         return a+txt[0]
#
# txt = input()
# print(spell(txt)) #INPUT=HELLO, OUTPUT=OLLEH
# ---------------------------------------------------------------------------------------
# squares numbers with function
# def sq(n):
#     if n == 1:
#         return n
#     else:
#         return n**2 + sq(n-1)
#
# print(sq(5))
# # squares number from lambda
# sq=lambda n: n if n==1 else n**2 + sq(n-1)
# print(sq(5))
# --------------------------------------------/
# a=int(input("enter the number"))
# b=int(input("enter the 2nd number"))
# c=int(input("enter the 3rd number"))
# if a>b and a>c:
#     if b>c:
#         print("a is greater")
#     else:
#         print("c is greater")
# else:
#     print("b is greater")
#-----------------------------------------
# a=int(input("enter the number"))
# if a>5 and a<10:
#     if a==7:
#         if a<=8:
#             print("yes it is less than 8")
#         else:
#             print("enter the number again")
#     else:
#         print(" ** enter the number again")
# elif a>=12:
#     print("number is greater ")
# else:
#     print("enter the number again")
#----------------------------------------------
#list1=[["rohit",24],["shubham",23],["dhruv",24],["vishal",24],["amartya",24],["vishwajit",23]]
# set1=set()
# set1.add("rohit")
# set1.add("kumar")
# print(set1)
# set2=list(set1)
# print(set2)
# set1={"apple","mango",["banana"],["cherry"]}
# print(set1)
#===============================================
# list1=[ 1,4,3,5,2,24,3,55,23,54,6]
# for item in list1:
#     if str(item).isnumeric() and item>6:
#         print(item)

i=0
while(i<45):
    i+=1
    if i < 4:
        print("yes it is less than",i, end=" ")
    else:
        print("get out ",i, end=" ")

# ===================================================================
# list1=[1,23,4,4,5,5]
# for number in list1:
#     print(number,end=" ")

# i=0
# while(True):
#     print(i+1)
#     if(i==10):
#         break
#     i+=1

# c=lambda a,b:a+b
# print(c(4,6))
# z=lambda x,y:\
#     x+y
# print(z(3,5))

# class student:
#     x=5
#     print(x)
#
# s1=student
# y=s1.x
# print(y)

# a="7"
# b="8"
# print(int(a)+int(b))
# print("enter the number")
# num=input()
# print(int(num)+10)
# tuple1=tuple()
# tuple1="rohit","kumar","amit"
# print(tuple1)
# list1=tuple1
# list1=list()
# print(list1)
# list1="rohit","amit","amit"
# print(list1)
# a=7
# b=8
# temp=a
# a=b
# b=temp
# print(a,b)
# dict1=dict
# dict1={"name":"rohit"}
# dict1.update({"name2":"amit"})
# dict1["name3"]="poja"
# dict1["name4"]="kusum"
# print(dict1)
# string1="red black blue maroon"
# print(string1.split())
# def add(**name): #key= value
#     print(name)
#
# add(name="rohit",surname="kumar")
# add(android="samsung",book="python")
# i=0
# while(True):
#
#     if(i<10):
#         i=i+1
#         print(i)
#         continue
#     print(i)
#     if i==20:
#         break
#     i=i+1
#continue= stop the current iteration and run the next, break = when condition is true the its stop execution
# while True:
#     num = int(input("enter the number\n"))
#     if num>50:
#         print("yes you entered the right number")
#         break
#     elif num==50:
#         print("both are equal")
#
#     else:
#         print(num,"\n enter the number again")
#         continue
# ==========================================================================
#Arithmetic operation
# print("2+4",2+4)
# print("2-4",2-4)
# print("2*4",2*4)
# print("2/4",2/4)
# print("2%4",2%4)
# print("2**4",2**4)
# print("2//25",2//25)
#Assignment operator

#Coomparison operator

#Identity operators
#Membership operators
#Logical operators
# a=True
# b=False
# print(not(a or  b))
# c=False
# d=False
# print(not(c or d))
# x=True
# y=True
# print(not(x or y))
# p=False
# q=True
# print(not(p or q))
# Bitwise operator
# print(bool(1&2))
# print(bool(3|2))
# a=int(input("enter the number"))
# b=int(input("enter the number"))
# print("a is greater than b") if a>b else print("b is greater than a")
# a=9
# b=7
# try:
#     print(a + b)
# except Exception as e:
#     print(e,"this is important line")
#     print("ok i got the error")
# else:
#     print("i got no error in try block")
# =======================================

# try:
#     print("a is greater then b") if a>b else print("b is greater than a")
# except Exception as e:
#     print("NOT DEFINED")
#     print("hello")
# else:
#     print("if no error found then will execute else statement")
# finally:
#     print("main nahi rukunga meri marzi")
# --------------------------------------------------------------
# def is_inverse(word,word1):
#     if len(word) != len(word1):
#         return False
#     i=0
#     j=len(word1)-1
#     while j>0:
#         if word[i]==word1[j]:
#             return False
#
#         i = i + 1
#         j = j - 1
#
#     return True
#
# z=is_inverse("rohit","sphit")
# print(z)
# ==============================================================
# lis = []
# s=input("Enter String")
# for ch in s:
#     if ch in lis:
#         lis.append('$')
#     else:
#         lis.append (ch)
# print(''.join(str(i) for i in lis))
# ==================================================
# def is_even(striing):
#     print(striing)
#
# x=map(is_even,("r","o","h"))
# print(x)
###################################################
# Write a Python program to count the number of characters (character frequency) in a string. Go to the editor
# Sample String : google.com' Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1} By dictionary
# def count(string):
#     dict={}
#     for n in string:
#         keys=dict.keys()
#         if n in keys:
#             dict[n]=dict[n]+1
#         else:
#             dict[n]=1
#     return dict
#
# a=count("google")
# print(a)
#############################################################
# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead of the empty string
# def first_last(string):
#     string2=string[0:2] + string[-2:]
#     print(string2)
#     if len(string2)<2:
#         return "empty"
#     else:
#         return "is greater"

# z=first_last("google")
# print(z)
#####################################################################
# Write a Python program to get a string from a given string where all occurrences of its first char have been
# changed to '$', except the first char itself.
# def special(string):
#
#     char=string[1]
#     string2=string.replace(char,"$")
#     print(string2)
#     string1=string[0]+char+string2[2:]
#     return string1
#
# x=special("google")
# print(x)
######################################################################
# Write a Python program to get a single string from two given strings, separated by a space and swap
# the first two characters of each string. Example=abc,xyz: xyc:abz
# def new_String(a,b):
#     char=b[0:2]+a[-1]
#     char1=a[0:2]+b[-1]
#     return char+" "+char1
#
# d=new_String("abc","xyz")
# print(d)
####################################################
# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string,
# if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string
# Sample String : 'The lyrics is not that poor!'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'The lyrics is poor!'
# def appearance(str):
#     char="good"
#     string=str.find("not")
#     string1=str.find("poor")
#     if string1>string:
#         string2=str.replace(str[string:string1+4],char)
#         print(string2)
#
# appearance("The lyrics is not that poor! The lyrics is poor!'")
###############################################################
# Write a Python program to remove the nth index character from a nonempty string
# def strings(string,n):
#     first_part=string[:n]
#     second_part=string[n+1:]
#     main_string=first_part+second_part
#     print(main_string)
# if __name__ == '__main__':
#     strings("python",4)
####################################################
# Write a Python program to change a given string to a new string where the first and last chars have been exchanged
# def string(word):
#     print(word)
#     return word[-1:]+word[1:-1]+word[0:1]
#
# exchanged=input("enter the word, want to exchanged")
# a=string(exchanged)
# print(a)
##############################################
# Write a Python function that takes a list of words and returns the length of the longest one.
# def length(list1):
#     list=[]
#     for i in list1:
#         list.append((len(i),i))
#         list.sort()
#     print(list[-1])
#
# length(["apple","pineapple","mango"])
# ====================================================
# Write a Python program to remove the characters which have odd index values of a given string.
# def string(word):
#     for i in range(len(word)):
#         if i%2==0:
#             result=word[i]
#             print(result,end="")
# a=input("enter the word")
# string(a)
# ========================================================
# Write a Python program to count the occurrences of each word in a given sentence
# def count(word):
#     dict={}
#     for i in word.split():
#         keys=dict.keys()
#         if i in keys:
#             dict[i]=dict[i]+1
#         else:
#             dict[i]=1
#     return dict
# b=input("enter the string:")
# a=count(b)
# print(a)
# =============================================================
# Write a Python script that takes input from the user and displays that input back in upper and lower cases.
# string=input("enter the string")
# print(string.upper())
# print(string.lower())
# +++++++++++++++++++++++++++==========================+++++++++++++++
# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in
# sorted form (alphanumerically).Sample Words:red, white, black, red, green, black,Expected Result : black, green, red,
# white,red==here, we have taken a list from user and prints it in alphabatically
# def sep_comma(num):
#     list=[]
#     for i in range(num):
#         list.append(input("enter the item"))
#     for i in list:
#             list.sort()
#     print(list)
#
# a=int(input("enter the count"))
# sep_comma(a)
# ===============================================================/
# Write a Python function to insert a string in the middle of a string.
# def insert_word(string,number,word1):
#     string=string.split()
#     string.insert(number,word1)
#     print(string)
#
# sentense=input("enter the word")
# index=int(input("enter the index"))
# word=input("enter the word")
# insert_word(sentense,index,word)
# ====================================================
#  Write a Python function to get a string made of 4 copies of the last two characters of a specified string (
#  length must be at least 2). Go to the editor. Sample function and result :insert_end('Python') -> onononon
# insert_end('Exercises') -> eseseses
# def four_copies(str):
#     char=str[-2:]
#     # space=""
#     i=0
#     while i < 4:
#         main=char+""
#         print(main,end="")
#         i=i+1
# string = input("enter the word")
# four_copies(string)
# =================================================
# Write a Python function to get a string made of its first three characters of a specified string. If the length of
# the string is less than 3 then return the original string. Go to the editor.
# Sample function and result :first_three('ipy') -> ipy//first_three('python') -> pyt
# def return_original(str):
#     if len(str)>3:
#         return str
#     else:
#         return str
#
# word=input("enter the word")
# a=return_original(word)
# print(a)
# =================================================
# word="geeksforgeeks"
# char=word[0:3]
# space=""
# a=word.replace(char,space)
# b=space+word[3:]
# print(b)
# =============================================================
# 19. Write a Python program to get the last part of a string before a specified character.
# https://www.w3resource.com/python-exercises=https://www.w3resource.com/python
# def link(string):
#     a=string.split("-")
#     b=a[-1]
#     string=string.replace(b,"")
#     return string
#
# f=link("https://www.w3resource.com/python-exercises")
# print(f)   #OUTPUT=https://www.w3resource.com/python-
# ======================================================================/
# 20. Write a Python function to reverses a string if it's length is a multiple of 4
# def reverse(string):
#     a = len(string)
#     if a % 4 == 0:
#         while a >0 :
#             b = string[a-1]
#             print(b)
#             a=a-1
#     else:
#         print("u enter the word is not a multiples of 4")
# word=input("enter the word")
# reverse(word)
# 2nd way use of join
# def reverse1(word1):
#     if len(word1)%4==0:
#         return "".join(reversed(word1))
#     return word1
#
# a=reverse1("amit")
# print(a)
# =================================================================================//
# 21. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase
# characters in the first 4 characters
# def string_IN_uppercase(string):
#     Count_UpperCase=0
#     for i in string[:4]: #for i in string[0:]
#         if i.upper()==i:
#             Count_UpperCase=Count_UpperCase+1
#         if Count_UpperCase>=2:
#             return string.upper()
#     return string
# word=input("enter the word")
# a=string_IN_uppercase(word)
# print(a)
# ===================================================/
# Write a Python program to sort a string lexicographically. sort the string
# def lexicographically(string):
#     a=list(string)
#     a.sort()
#     return a
# b=lexicographically("python3")
# print(b)
# =====================================================================/
# 23. Write a Python program to remove a newline in Python.
# string="Python Exercise\n"
# print(string.strip())
# ==================================================================
# 38. Write a Python program to count occurrences of a substring in a string
# string="is available at the bottom of the page to write and execute"
# print(string.count("the"))
# 39. Write a Python program to reverse a string.
# string="javascript"
#1st method
# print(string[::-1])
# 2nd method
# print("".join(sorted(string)))
# 3rd method
# string="rohit"
# i=5
# while i>0:
#     print(string[i-1])
#       i=i-1
# ====================================================================
# 40. Write a Python program to reverse words in a string
# string="means start at the end of the string and end "
# string=string.split()
# print(string[::-1])
# ===================================================================================
# 41. Write a Python program to strip a set of characters from a string
# remove vowels from string
# def remove_strip(str,vowel):
#     for i in str:
#         if i not in vowels:
#             str=i
#             print(str,end="")
#
# string="the quick brown fox"
# vowels="aeiou"
# remove_strip(string,vowels)
# remove vowels from string by join method
# def remove_strip(str,char):
#     print("".join(c for c in str if c not in char))
#
# string="the quick brown fox"
# character="aeiou"
# remove_strip(string,character)
# ================================================================/
# 42. Write a Python program to count repeated characters in a string.
# Sample string: 'thequickbrownfoxjumpsoverthelazydog' by dict function
# def repeated_string(str):
#     dict1 = dict()
#     for x in string:
#         if x in dict1:
#             dict1[x]=dict1[x]+1
#         else:
#             dict1[x]=1
#     return dict1
#
# string="thequickbrownfoxjumpsoverthelazydog"
# a=repeated_string(string)
# print(a)
# 2nd way by dict
# def repeated_string(str):
#     dict={}
#     for i in str:
#         if i in dict:
#             dict[i]=dict[i]+1
#         else:
#             dict[i]=1
#     return dict
#
# string="the quick brown fox jumps over the lazy dog"
# a=repeated_string(string)
# print(a)
# ===============================================
element="rohit"
for i in reversed(element):
    print(i)







