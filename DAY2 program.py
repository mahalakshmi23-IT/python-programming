#Identify the Nature of a Number
n=int(input())
if n>0:
  print("POSITIVE")
elif  n<0:
  print("NEGATIVE")
else:
  print("ZERO")
  
#Explore Math Functions
import math
a=float(input())
b=int(input())
c=int(input())
d=int(input())
print(math.floor(a))
print(math.ceil(a))
print(round(a))
print(int(math.sqrt(b)))
print(c**d)

#Smallest of Four Numbers
a=int(input())
b=int(input())
c=int(input())
d=int(input())
print(min(a,b,c,d))

#Truncate to Two Decimal Places
import math
n=float(input())
print(f"{math.trunc(n*100)/100:.2f}")

#Find Second Maximum Number
a = int(input())
b = int(input())
c = int(input())

if a > b:
    if b > c:
        print(b)
    else:
        if a > c:
            print(c)
        else:
            print(a)
else:
    if a > c:
        print(a)
    else:
        if b > c:
            print(c)
        else:
            print("No second max")

#Triangle Angle Validation

A=int(input())
B=int(input())
C=int(input())
if A + B + C == 180 and A > 0 and B > 0 and C > 0:
    print("VALID")

    if A == B == C:
        print("EQUILATERAL")
    elif A == B or B == C or A == C:
        print("ISOSCELES")
    else:
        print("SCALENE")
else:
    print("NOT VALID")

#Number to Word
n=int(input())
if n==0:
  print("zero")
elif n==1:
  print("one")
elif n==2:
  print("two")
elif n==3:
  print("three")
elif n==4:
  print("four")
elif n==5:
  print("five") 
elif n==6:
  print("six")  
elif n==7:
  print("seven")
elif n==8:
  print("eight")
elif n==9:
  print("nine")
else:
  print("invalid")
  #Vowel or Consonant
ch=input()
if ch in ('a','e','i','o','u','A','E','I','O','U') :
  print("vowel")
else:
  print("consonant")
#Leap Year Checker
a=int(input())
if a%400==0 or (a%4==0 and a%100 !=0):
  print("yes")
else:
  print("no")
#Fun Grade Calculator
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
Average=(a+b+c+d+e)/5
if Average>=90:
  print("Excellent!")
elif (Average >= 80) :
  print("Great Job!")
elif (Average >= 70) :
  print("Good Effort!")
elif (Average >= 50) :
  print("Keep Trying!")
else:
  print("Better Luck Next Time!")

#Train Berth Type Finder
seat=int(input())
no=seat%8
match no:
  case 1:
    print("LB")
  case 2:
    print("MB")
  case 3:
    print("UB")
  case 4:
    print("LB")
  case 5:
    print("MB")
  case 6:
    print("UB")
  case 7:
    print("SL")
  case 0:
    print("SU")

#Electricity Bill Calculator
n = int(input())
if n <= 50:
    bill = n * 1
elif n <= 150:
    bill = 50 + (n - 50) * 2
elif n <= 250:
    bill = 50 + 200 + (n - 150) * 3
else:
    bill = 50 + 200 + 300 + (n - 250) * 4
if bill > 150:
    bill = bill + (bill * 20 / 100)
print(int(bill))

#Thala vs Thalapathy Game
n=int(input())
if n%3==0 and n%5!=0:
  print("Thala")
elif n%5==0 and n%3!=0:
  print("Thalapathy")
elif n%3==0 and n%5==0:
  print("ThalaThalapathy")
elif n%3!=0 or n%5!=0:
  print(n)

#Train Fare Calculator

age=int(input())
km=int(input())
if age<12:
  print(int(km*2.5))
elif age<=12 or age<=59:
  print(int(km*5))
elif age>=60:
  print(int(km*3.75))

#Average Marks Calculator
a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
av=(a+b+c+d+e)/5
if av.is_integer():
  print(int(av))
else:
  print(f"{av:.2f}")
#Fun Character Case Converter
a=input()
if a in "abcdefghijklmnopqrstuvwxyz":
  print(a.upper())
elif a in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
  print(a.lower())
else:
  print("abcd theriyatha?")





 

  
  





