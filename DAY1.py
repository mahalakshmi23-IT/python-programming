#ASCII
n = int(input())
print(chr(n))

#Update Counter
a=int(input())
print(((a+5)*2)-3)

#ODD or EVEN
n = int(input())
print("Even" if n%2==0 else "Odd")

#Greatest Among Three Numbers
a=int(input())
b=int(input())
c=int(input())
print(max(a,b,c))

#Character Digit to Integer
a=input()
print(int(a))

#Personalized Greeting
a=str(input())
print(f"Hi {a}, welcome to the programming class!")

#Calculate Total and Average Marks
a=str(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())
g=(b+c+d+e+f)/5
print("Student Name:",a)
print("Total Marks:",b+c+d+e+f)
print("Average Marks:",(f"{g:.2f}"))

#Shape Area Calculation
a = int(input())
l = int(input())
b = int(input())
r = int(input())
B = int(input())
h = int(input())
square = a * a
rectangle = l * b
circle = 3.14 * r * r
triangle = 0.5 * B * h
print("Area of Square=", square, sep="")
print("Area of Rectangle=", rectangle, sep="")
print(f"Area of Circle={circle:.2f}")
print("Area of Triangle=", int(triangle) if triangle.is_integer() else triangle, sep="")

#Shape Perimeter Calculation Program
a=int(input())
l=int(input())
w=int(input())
r=int(input())
side1=int(input())
side2=int(input())
base=int(input())
Square=4*a
Rectangle=2*(l + w)
Circle=2*3.14*r
Triangle=side1+base+side2
print(Square)
print(Rectangle)
print(f"{Circle:.2f}")
print(Triangle)

#Handling Mixed Inputs
a=int(input())
b=input()
print(a)
print(b)











